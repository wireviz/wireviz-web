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
from pathlib import PurePath

import werkzeug
from flask import Blueprint, request
from flask_restx import Api, Resource, reqparse

from wireviz_web import __version__
from wireviz_web.core import decode_plantuml, mimetype_to_type, send_image

file_upload = reqparse.RequestParser()
file_upload.add_argument(
    "yml_file",
    type=werkzeug.datastructures.FileStorage,
    location="files",
    required=True,
    help="YAML file",
)

wireviz_blueprint = Blueprint("wireviz-web", __name__)
api = Api(
    app=wireviz_blueprint,
    version=__version__,
    title="WireViz-Web",
    description="A wrapper around WireViz for bringing it to the web. "
    "Easily document cables and wiring harnesses.",
    doc="/doc",
    catch_all_404s=True,
)

ns = api.namespace("", description="WireViz-Web REST API")


@ns.route("/render")
class Render(Resource):
    @api.expect(file_upload)
    @ns.produces(["image/svg+xml", "image/png"])
    def post(self):
        """"""

        mimetype = request.headers.get("accept")

        args = file_upload.parse_args()
        yaml_input = args["yml_file"].read()

        input_filename = args["yml_file"].filename
        output_filename = (
            PurePath(PurePath(input_filename).stem)
            .with_suffix("." + mimetype_to_type(mimetype))
            .name
        )

        return send_image(
            input_yaml=yaml_input,
            output_mimetype=mimetype,
            output_filename=output_filename,
        )


@ns.route("/png/<encoded>")
@ns.param("encoded", "encoded script like plantuml uses")
class PNGRender(Resource):
    @ns.produces(["image/png"])
    def get(self, encoded):
        """"""
        yaml_input = decode_plantuml(input_plantuml=encoded)
        return send_image(
            input_yaml=yaml_input,
            output_mimetype="image/png",
            output_filename="png_rendered.svg",
        )


@ns.route("/svg/<encoded>")
@ns.param("encoded", "encoded script like plantuml uses")
class SVGRender(Resource):
    @ns.produces(["image/sgv+xml"])
    def get(self, encoded):
        """"""
        yaml_input = decode_plantuml(input_plantuml=encoded)
        return send_image(
            input_yaml=yaml_input,
            output_mimetype="image/svg+xml",
            output_filename="svg_rendered.svg",
        )
