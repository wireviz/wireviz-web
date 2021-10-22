# A wrapper around WireViz for bringing it to the web. Easily document cables and wiring harnesses.
#
# Copyright (C) 2020  Jürgen Key <jkey@arcor.de>
# Copyright (C) 2021  Andreas Motl <andreas.motl@panodata.org>
#
# This program is free software: you can redistribute it and/or modify
# it under the terms of the GNU Affero General Public License as published by
# the Free Software Foundation, either version 3 of the License, or
# (at your option) any later version.
#
# This program is distributed in the hope that it will be useful,
# but WITHOUT ANY WARRANTY; without even the implied warranty of
# MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE.  See the
# GNU Affero General Public License for more details.
#
# You should have received a copy of the GNU Affero General Public License
# along with this program.  If not, see <http://www.gnu.org/licenses/>.
#
import io
import json
import logging
from pathlib import Path
from tempfile import NamedTemporaryFile

import yaml
from flask import Response, send_file
from werkzeug.exceptions import BadRequest, NotAcceptable
from wireviz import wireviz
from wireviz.Harness import Harness
from wireviz.wv_bom import bom_list
from wireviz.wv_helper import tuplelist2tsv

from wireviz_web.plantuml import plantuml_decode
from wireviz_web.util import ReversibleDict

mimetype_type_map: ReversibleDict = ReversibleDict(
    {
        "image/png": "png",
        "image/svg+xml": "svg",
        "text/html": "html",
        "text/plain": "bom.txt",
        "application/json": "bom.json",
    }
)

logger = logging.getLogger(__name__)


def mimetype_to_type(mime_type: str) -> str:
    """
    Translate MIME type to output type.
    For unknown types, raise HTTP Not Acceptable.

    :param mime_type: The MIME type string.
    :return:          The image type string.
    """
    try:
        return mimetype_type_map[mime_type]
    except KeyError:
        raise NotAcceptable(description=f"Output type not acceptable: {mime_type}")


def type_to_mimetype(output_type: str) -> str:
    """
    Translate output type to MIME type.
    For unknown types, raise HTTP Not Acceptable.

    :param output_type: The output type string.
    :return:            The MIME type string.
    """
    try:
        return mimetype_type_map.lookup(output_type)
    except KeyError:
        raise NotAcceptable(description=f"Output type not acceptable: {output_type}")


def decode_plantuml(input_plantuml: str) -> str:
    """
    Decode PlantUML Text Encoding format.

    See also: https://plantuml.com/text-encoding

    :param input_plantuml: The request data, encoded with PlantUML Text Encoding format.
    :return:               The decoded data.
    """
    try:
        return plantuml_decode(input_plantuml)
    except Exception as ex:
        raise BadRequest(description=f"Unable to decode PlantUML Text Encoding format: {ex}")


def wireviz_render(input_yaml: str, output_mimetype: str, output_filename: str) -> Response:
    """
    Render WireViz output and create a Flask Response.

    :param input_yaml:      Input data in WireViz YAML format.
    :param output_mimetype: The designated output format mimetype. Currently available:
                            - image/svg+xml
                            - image/png
                            - text/html
                            - text/plain
                            - application/json
    :param output_filename: The designated output filename.
    :return:                A Flask Response object.
    """

    # Sanity checks.
    if not input_yaml.strip():
        raise BadRequest(description="No input data")

    # Compute output type from MIME type.
    return_type = mimetype_to_type(output_mimetype)

    # Parse WireViz YAML.
    try:
        harness: Harness = wireviz.parse(yaml_input=input_yaml, return_types="harness")
    except Exception as ex:
        message = f"Unable to parse WireViz YAML format: {ex}"
        logger.exception(message)
        raise BadRequest(description=message)

    # Dispatch rendering by designated output type.
    if return_type == "png":
        payload = harness.png

    elif return_type == "svg":
        payload = harness.svg

    elif return_type == "html":
        try:
            tmpfile = NamedTemporaryFile(delete=False)

            # Build list of implicitly created temporary files.
            tempfiles = []
            for suffix in [".gv", ".png", ".svg", ".bom.tsv", ".html"]:
                tempfiles.append(f"{tmpfile.name}{suffix}")

            # Render HTML output.
            harness.output(filename=tmpfile.name, fmt=("png", "svg"))
            with open(f"{tmpfile.name}.html", "rb") as f:
                payload = f.read()

        except Exception as ex:  # pragma: no cover
            message = f"Unable to produce WireViz output: {ex}"
            logger.exception(message)
            raise BadRequest(description=message)

        finally:
            # Clean up temporary files.
            for tempfile in tempfiles:
                try:
                    Path(tempfile).unlink(missing_ok=True)
                except (FileNotFoundError, TypeError):  # pragma: no cover
                    pass

    elif return_type == "bom.txt":
        harness.create_graph()
        bomlist = bom_list(harness.bom())
        payload = tuplelist2tsv(bomlist).encode("utf-8")

    elif return_type == "bom.json":
        harness.create_graph()
        bomlist = bom_list(harness.bom())
        payload = json.dumps(bomlist, indent=2).encode("utf-8")

    # Respond with rendered image.
    return send_file(
        io.BytesIO(payload),
        mimetype=output_mimetype,
        as_attachment=True,
        download_name=output_filename,
    )
