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
        assert response.status_code == 500
        assert response.json == {
            "exception": "'HTTP_ACCEPT'",
            "message": "internal error",
        }

    def test_error_no_data(self, client):
        response = client.post(
            url_for("wireviz-web._render"),
            headers={"Accept": ""},
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
            headers={"Accept": ""},
        )
        assert response.status_code == 500
        assert response.json == {
            "exception": "'str' object does not support item assignment",
            "message": "internal error",
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
        assert b"<title>404 Not Found" in response.data

    def test_svg_invalid_data(self, client):
        response = client.get(
            url_for("wireviz-web._svg_render", encoded=self.data_invalid),
        )
        assert response.status_code == 500
        assert response.json == {
            "exception": "'str' object does not support item assignment",
            "message": "internal error",
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
        assert b"<title>404 Not Found" in response.data

    def test_png_invalid_data(self, client):
        response = client.get(
            url_for("wireviz-web._png_render", encoded=self.data_invalid),
        )
        assert response.status_code == 500
        assert response.json == {
            "exception": "'str' object does not support item assignment",
            "message": "internal error",
        }

