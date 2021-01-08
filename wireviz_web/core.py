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


def mimetype_to_type(mimetype: str) -> str:
    if mimetype == "image/svg+xml":
        return "svg"
    elif mimetype == "image/png":
        return "png"
    else:
        raise NotAcceptable(
            description="Output type not acceptable: {}".format(mimetype)
        )


def decode_plantuml(input_plantuml: str) -> str:
    try:
        return plantuml_decode(input_plantuml)
    except Exception as ex:
        raise BadRequest(
            description="Unable to parse PlantUML request format: {}".format(ex)
        )


def send_image(input_yaml: str, output_mimetype: str, output_filename: str) -> Response:

    if not input_yaml.strip():
        raise BadRequest(description="No input data")

    return_type = mimetype_to_type(output_mimetype)

    try:
        payload = wireviz.parse(input_yaml, return_types=return_type)
    except Exception as ex:
        raise BadRequest(
            description="Unable to parse WireViz YAML format: {}".format(ex)
        )

    return send_file(
        io.BytesIO(payload),
        mimetype=output_mimetype,
        as_attachment=True,
        attachment_filename=output_filename,
    )
