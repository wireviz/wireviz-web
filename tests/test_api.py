import io

import filetype
from flask import url_for

from wireviz_web.plantuml import plantuml_encode


class TestRenderRegular:
    @property
    def data_valid(self):
        return {"yml_file": (io.BytesIO(b"Bob -> Alice : hello"), "test.yml")}

    @property
    def data_invalid(self):
        return {"yml_file": (io.BytesIO(b"foobar"), "invalid.yml")}

    def test_svg(self, client):
        response = client.post(
            url_for("wireviz-web._render"),
            data=self.data_valid,
            headers={"Accept": "image/svg+xml"},
        )
        assert response.status_code == 200
        assert b"""<?xml version="1.0" """ in response.data
        assert b"<!DOCTYPE svg PUBLIC" in response.data
        assert b"<svg " in response.data
        assert b"<polygon " in response.data

    def test_png(self, client):
        response = client.post(
            url_for("wireviz-web._render"),
            data=self.data_valid,
            headers={"Accept": "image/png"},
        )
        assert response.status_code == 200
        assert filetype.guess(response.data).mime == "image/png"

    def test_error_no_accept(self, client):
        response = client.post(
            url_for("wireviz-web._render"),
            data=self.data_valid,
        )
        assert response.status_code == 406
        assert response.json == {
            "message": "Output type not acceptable: None",
        }

    def test_error_empty_accept(self, client):
        response = client.post(
            url_for("wireviz-web._render"),
            data=self.data_valid,
            headers={"Accept": ""},
        )
        assert response.status_code == 406
        assert response.json == {
            "message": "Output type not acceptable: ",
        }

    def test_error_no_data(self, client):
        response = client.post(
            url_for("wireviz-web._render"),
            headers={"Accept": "image/svg+xml"},
        )
        assert response.status_code == 400
        assert response.json == {
            "errors": {
                "yml_file": "YAML file Missing required parameter in an uploaded file"
            },
            "message": "Input payload validation failed",
        }

    def test_error_invalid_data(self, client):
        response = client.post(
            url_for("wireviz-web._render"),
            data=self.data_invalid,
            headers={"Accept": "image/svg+xml"},
        )
        assert response.status_code == 400
        assert response.json == {
            "message": "Unable to parse WireViz YAML format: 'str' object does not support item assignment",
        }


class TestRenderPlantUML:
    @property
    def data_valid(self):
        return plantuml_encode("Bob -> Alice : hello")

    @property
    def data_invalid(self):
        return plantuml_encode("foobar")

    def test_svg_success(self, client):
        response = client.get(
            url_for("wireviz-web._svg_render", encoded=self.data_valid),
        )
        assert response.status_code == 200
        assert b"""<?xml version="1.0" """ in response.data
        assert b"<!DOCTYPE svg PUBLIC" in response.data
        assert b"<svg " in response.data
        assert b"<polygon " in response.data

    def test_svg_no_data(self, client):
        response = client.get(
            url_for("wireviz-web._svg_render", encoded=""),
        )
        assert response.status_code == 404
        assert response.json["message"].startswith(
            "The requested URL was not found on the server."
        )

    def test_svg_invalid_raw_data(self, client):
        response = client.get(
            url_for("wireviz-web._svg_render", encoded="foobar"),
        )
        assert response.status_code == 400
        assert response.json == {
            "message": "Unable to decode PlantUML Text Encoding format: Incorrect padding",
        }

    def test_svg_invalid_encoded_data(self, client):
        response = client.get(
            url_for("wireviz-web._svg_render", encoded=self.data_invalid),
        )
        assert response.status_code == 400
        assert response.json == {
            "message": "Unable to parse WireViz YAML format: 'str' object does not support item assignment",
        }

    def test_png_success(self, client):
        response = client.get(
            url_for("wireviz-web._png_render", encoded=self.data_valid),
        )
        assert response.status_code == 200
        assert filetype.guess(response.data).mime == "image/png"

    def test_png_no_data(self, client):
        response = client.get(
            url_for("wireviz-web._png_render", encoded=""),
        )
        assert response.status_code == 404
        assert response.json["message"].startswith(
            "The requested URL was not found on the server."
        )

    def test_png_invalid_raw_data(self, client):
        response = client.get(
            url_for("wireviz-web._png_render", encoded="foobar"),
        )
        assert response.status_code == 400
        assert response.json == {
            "message": "Unable to decode PlantUML Text Encoding format: Incorrect padding",
        }

    def test_png_invalid_encoded_data(self, client):
        response = client.get(
            url_for("wireviz-web._png_render", encoded=self.data_invalid),
        )
        assert response.status_code == 400
        assert response.json == {
            "message": "Unable to parse WireViz YAML format: 'str' object does not support item assignment",
        }
