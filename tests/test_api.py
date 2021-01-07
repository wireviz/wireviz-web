import io

import filetype
from flask import url_for

from wireviz_web.plantuml import plantuml_encode


class TestRenderRegular:
    @property
    def data(self):
        return {"yml_file": (io.BytesIO(b"Bob -> Alice : hello"), "test.yml")}

    def test_svg(self, client):
        response = client.post(
            url_for("wireviz-web._render"),
            data=self.data,
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
            data=self.data,
            headers={"Accept": "image/png"},
        )
        assert response.status_code == 200
        assert filetype.guess(response.data).mime == "image/png"


class TestRenderPlantUML:
    @property
    def data(self):
        return plantuml_encode("Bob -> Alice : hello")

    def test_svg(self, client):
        response = client.get(
            url_for("wireviz-web._svg_render", encoded=self.data),
        )
        assert response.status_code == 200
        assert b"""<?xml version="1.0" """ in response.data
        assert b"<!DOCTYPE svg PUBLIC" in response.data
        assert b"<svg " in response.data
        assert b"<polygon " in response.data

    def test_png(self, client):
        response = client.get(
            url_for("wireviz-web._png_render", encoded=self.data),
        )
        assert response.status_code == 200
        assert filetype.guess(response.data).mime == "image/png"
