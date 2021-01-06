# A wrapper around WireViz for bringing it to the web. Easily document cables and wiring harnesses.
#
# Copyright (C) 2020  Jürgen Key <jkey@arcor.de>
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
import os
import tempfile

import werkzeug
from flask import Blueprint, jsonify, make_response, request, send_file
from flask_restplus import Api, Resource, reqparse
from wireviz import wireviz

from wireviz_web.plantuml import plantuml_decode

file_upload = reqparse.RequestParser()
file_upload.add_argument('yml_file',
                         type=werkzeug.datastructures.FileStorage,
                         location='files',
                         required=True,
                         help='YAML file')

wireviz_blueprint = Blueprint('wireviz-web', __name__)
api = Api(wireviz_blueprint, doc='/doc', version='0.0.0', title='WireViz-Web',
          description='WireViz-Web is building on WireViz for easily documenting cables, '
                      'wiring harnesses and connector pinouts.', )

ns = api.namespace('', description='WireViz-Web REST API')


@ns.route('/render')
class Render(Resource):
    @api.expect(file_upload)
    @ns.produces(['image/png', 'image/svg+xml'])
    def post(self):
        """
        """
        args = file_upload.parse_args()
        try:
            file_temp=tempfile.TemporaryFile()
            args['yml_file'].save(file_temp)
            filename=os.path.splitext(os.path.basename(os.path.normpath(args['yml_file'].filename)))[0]
            print(filename)
            file_temp.seek(0)
            yaml_input = file_temp.read().decode()
            file_out=tempfile.NamedTemporaryFile()
            fon="%s%s" % (file_out.name, '.png')
            outputname = "%s%s" % (fon, '.png')
            resultfilename="%s%s" % (filename, '.png')
            mimetype='image/png'
            if request.headers["accept"] == "image/svg+xml":
                fon="%s%s" % (file_out.name, '.svg')
                outputname="%s%s" % (fon, '.svg')
                mimetype='image/svg+xml'
                resultfilename="%s%s" % (filename, '.svg')
            wireviz.parse(yaml_input, file_out=fon)
            return send_file(outputname,
                                     as_attachment=True,
                                     attachment_filename=resultfilename,
                                     mimetype=mimetype)
        except Exception as e:
            print(e)
            return make_response(jsonify({
                'message': 'internal error',
                'exception': str(e)
            }), 500)


@ns.route('/png/<encoded>')
@ns.param('encoded', 'encoded script like plantuml uses')
class PNGRender(Resource):
    @ns.produces(['image/png'])
    def get(self,encoded):
        """
        """
        try:
            file_out=tempfile.NamedTemporaryFile()
            fon="%s%s" % (file_out.name, '.png')
            outputname = "%s%s" % (fon, '.png')
            resultfilename="%s%s" % ('png_rendered', '.png')
            mimetype='image/png'
            wireviz.parse(plantuml_decode(encoded), file_out=fon)
            return send_file(outputname,
                                     as_attachment=True,
                                     attachment_filename=resultfilename,
                                     mimetype=mimetype)
        except Exception as e:
            print(e)
            return make_response(jsonify({
                'message': 'internal error',
                'exception': str(e)
            }), 500)


@ns.route('/svg/<encoded>')
@ns.param('encoded', 'encoded script like plantuml uses')
class SVGRender(Resource):
    @ns.produces(['image/sgv+xml'])
    def get(self,encoded):
        """
        """
        try:
            file_out=tempfile.NamedTemporaryFile()
            fon="%s%s" % (file_out.name, '.svg')
            outputname = "%s%s" % (fon, '.svg')
            resultfilename="%s%s" % ('svg_rendered', '.svg')
            mimetype='image/svg+xml'
            print('/svg/<encoded>')
            print(resultfilename)
            wireviz.parse(plantuml_decode(encoded), file_out=fon)
            return send_file(outputname,
                                     as_attachment=True,
                                     attachment_filename=resultfilename,
                                     mimetype=mimetype)
        except Exception as e:
            print(e)
            return make_response(jsonify({
                'message': 'internal error',
                'exception': str(e)
            }), 500)
