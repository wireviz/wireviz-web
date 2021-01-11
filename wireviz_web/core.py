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

from flask import Response, send_file
from werkzeug.exceptions import BadRequest, NotAcceptable
from wireviz import wireviz

from wireviz_web.plantuml import plantuml_decode
from wireviz_web.util import ReversibleDict

mimetype_type_map: ReversibleDict = ReversibleDict(
    {
        "image/png": "png",
        "image/svg+xml": "svg",
    }
)


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
        raise NotAcceptable(description="Output type not acceptable: {}".format(mime_type))


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
        raise NotAcceptable(description="Output type not acceptable: {}".format(output_type))


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
        raise BadRequest(description="Unable to decode PlantUML Text Encoding format: {}".format(ex))


def send_image(input_yaml: str, output_mimetype: str, output_filename: str) -> Response:
    """
    Render an image using WireViz and create a Flask Response.

    :param input_yaml:      Input data in WireViz YAML format.
    :param output_mimetype: The designated output format mimetype
                            (either "image/svg+xml" or "image/png").
    :param output_filename: The designated output filename.
    :return:                A Flask Response object.
    """
    if not input_yaml.strip():
        raise BadRequest(description="No input data")

    return_type = mimetype_to_type(output_mimetype)

    # Render input YAML with WireViz.
    try:
        payload = wireviz.parse(yaml_input=input_yaml, return_types=return_type)
    except Exception as ex:
        raise BadRequest(description="Unable to parse WireViz YAML format: {}".format(ex))

    # Respond with rendered image.
    return send_file(
        io.BytesIO(payload),
        mimetype=output_mimetype,
        as_attachment=True,
        attachment_filename=output_filename,
    )
