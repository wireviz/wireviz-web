import io
from pathlib import Path

import filetype
import pytest
from flask import Response, url_for

from wireviz_web.plantuml import plantuml_encode


class TestRenderRegular:
    @property
    def data_valid(self):
        return {"yml_file": (io.BytesIO(b"Bob -> Alice : hello"), "test.yml")}

    @property
    def data_valid_with_title(self):
        return {"yml_file": (io.BytesIO(b"metadata:\n  title: Foobar\nBob -> Alice : hello"), "test.yml")}

    @property
    def data_empty(self):
        return {"yml_file": (io.BytesIO(b""), "empty.yml")}

    @property
    def data_invalid(self):
        return {"yml_file": (io.BytesIO(b"foobar"), "invalid.yml")}

    @property
    def data_demo01(self):
        here = Path(__file__).parent
        wireviz_yaml = open(here / "demo01.yaml", "rb").read()
        return {"yml_file": (io.BytesIO(wireviz_yaml), "test.yml")}

    def test_url(self, client):
        assert url_for("wireviz-web._render_regular") == "/render"

    def test_svg(self, client):
        response: Response = client.post(
            url_for("wireviz-web._render_regular"),
            data=self.data_valid,
            headers={"Accept": "image/svg+xml"},
        )
        assert response.status_code == 200
        assert response.headers["Content-Type"] == "image/svg+xml; charset=utf-8"
        assert response.headers["Content-Disposition"] == "attachment; filename=test.svg"
        assert b"""<?xml version="1.0" """ in response.data
        assert b"<!DOCTYPE svg PUBLIC" in response.data
        assert b"<svg " in response.data
        assert b"<polygon " in response.data

    def test_png(self, client):
        response = client.post(
            url_for("wireviz-web._render_regular"),
            data=self.data_valid,
            headers={"Accept": "image/png"},
        )
        assert response.status_code == 200
        assert response.headers["Content-Type"] == "image/png"
        assert response.headers["Content-Disposition"] == "attachment; filename=test.png"
        assert filetype.guess(response.data).mime == "image/png"

    def test_html(self, client):
        response = client.post(
            url_for("wireviz-web._render_regular"),
            data=self.data_valid,
            headers={"Accept": "text/html"},
        )
        assert response.status_code == 200

        assert response.headers["Content-Type"] == "text/html; charset=utf-8"
        assert response.headers["Content-Disposition"] == "attachment; filename=test.html"
        assert b"<!DOCTYPE html>" in response.data
        assert b"""<meta name="generator" content="WireViz""" in response.data
        assert b"<title>WireViz diagram and BOM</title>" in response.data
        assert b"<h2>Diagram</h2>" in response.data
        assert b"<svg" in response.data
        assert b"<h2>Bill of Materials</h2>" in response.data
        assert b"<table" in response.data

    def test_html_with_title(self, client):
        response = client.post(
            url_for("wireviz-web._render_regular"),
            data=self.data_valid_with_title,
            headers={"Accept": "text/html"},
        )
        assert response.status_code == 200

        assert b"<title>Foobar</title>" in response.data

    def test_bom_text(self, client):
        response = client.post(
            url_for("wireviz-web._render_regular"),
            data=self.data_demo01,
            headers={"Accept": "text/plain"},
        )
        assert response.status_code == 200
        assert response.headers["Content-Type"] == "text/plain; charset=utf-8"
        assert response.headers["Content-Disposition"] == "attachment; filename=test.bom.txt"
        reference = (
            b"Id\tDescription\tQty\tUnit\tDesignators\n"
            b"1\tCable, 3 x 0.25 mm\xc2\xb2 shielded\t0.2\tm\tW1\n"
            b"2\tConnector, D-Sub, female, 9 pins\t1\t\tX1\n"
            b"3\tConnector, Molex KK 254, female, 3 pins\t1\t\tX2\n"
        )
        assert reference == response.data

    def test_bom_json(self, client):
        response = client.post(
            url_for("wireviz-web._render_regular"),
            data=self.data_demo01,
            headers={"Accept": "application/json"},
        )
        assert response.status_code == 200
        assert response.headers["Content-Type"] == "application/json"
        assert response.headers["Content-Disposition"] == "attachment; filename=test.bom.json"
        reference = [
            ["Id", "Description", "Qty", "Unit", "Designators"],
            ["1", "Cable, 3 x 0.25 mm² shielded", "0.2", "m", "W1"],
            ["2", "Connector, D-Sub, female, 9 pins", "1", "", "X1"],
            ["3", "Connector, Molex KK 254, female, 3 pins", "1", "", "X2"],
        ]
        assert reference == response.json

    def test_error_no_accept(self, client):
        response = client.post(
            url_for("wireviz-web._render_regular"),
            data=self.data_valid,
        )
        assert response.status_code == 406
        assert response.json == {
            "message": "Output type not acceptable: None",
        }

    def test_error_empty_accept(self, client):
        response = client.post(
            url_for("wireviz-web._render_regular"),
            data=self.data_valid,
            headers={"Accept": ""},
        )
        assert response.status_code == 406
        assert response.json == {
            "message": "Output type not acceptable: ",
        }

    def test_error_wrong_accept(self, client):
        response = client.post(
            url_for("wireviz-web._render_regular"),
            data=self.data_valid,
            headers={"Accept": "image/jpg"},
        )
        assert response.status_code == 406
        assert response.json == {
            "message": "Output type not acceptable: image/jpg",
        }

    def test_invalid_no_data(self, client):
        response = client.post(
            url_for("wireviz-web._render_regular"),
            headers={"Accept": "image/svg+xml"},
        )
        assert response.status_code == 400
        assert response.json == {
            "errors": {"yml_file": "YAML file Missing required parameter in an uploaded file"},
            "message": "Input payload validation failed",
        }

    def test_invalid_empty_data(self, client):
        response = client.post(
            url_for("wireviz-web._render_regular"),
            data=self.data_empty,
            headers={"Accept": "image/svg+xml"},
        )
        assert response.status_code == 400
        assert response.json == {
            "message": "No input data",
        }

    def test_invalid_yaml_data(self, client):
        response = client.post(
            url_for("wireviz-web._render_regular"),
            data=self.data_invalid,
            headers={"Accept": "image/svg+xml"},
        )
        assert response.status_code == 400
        assert response.json == {
            "message": "Unable to parse WireViz YAML format: Expected a "
                       "dict as top-level YAML input, but got: <class 'str'>",
        }


class TestRenderPlantUML:
    @property
    def data_valid(self):
        return plantuml_encode("Bob -> Alice : hello")

    @property
    def data_invalid(self):
        return plantuml_encode("foobar")

    @pytest.mark.parametrize("imagetype", ["png", "svg"])
    def test_url(self, client, imagetype):
        assert url_for("wireviz-web._render_plant_uml", imagetype=imagetype, encoded=self.data_valid).startswith(
            f"/plantuml/{imagetype}"
        )

    def test_svg_success(self, client):
        response: Response = client.get(
            url_for("wireviz-web._render_plant_uml", imagetype="svg", encoded=self.data_valid),
        )
        assert response.status_code == 200
        assert response.headers["Content-Type"] == "image/svg+xml; charset=utf-8"
        assert response.headers["Content-Disposition"] == "attachment; filename=rendered.svg"
        assert b"""<?xml version="1.0" """ in response.data
        assert b"<!DOCTYPE svg PUBLIC" in response.data
        assert b"<svg " in response.data
        assert b"<polygon " in response.data

    def test_png_success(self, client):
        response = client.get(
            url_for("wireviz-web._render_plant_uml", imagetype="png", encoded=self.data_valid),
        )
        assert response.status_code == 200
        assert response.headers["Content-Type"] == "image/png"
        assert response.headers["Content-Disposition"] == "attachment; filename=rendered.png"
        assert filetype.guess(response.data).mime == "image/png"

    def test_error_empty_imagetype(self, client):
        response = client.get(
            url_for("wireviz-web._render_plant_uml", imagetype="", encoded=self.data_valid),
        )
        assert response.status_code == 404
        assert response.json["message"].startswith("The requested URL was not found on the server.")

    def test_error_wrong_imagetype(self, client):
        response = client.get(
            url_for("wireviz-web._render_plant_uml", imagetype="jpeg", encoded=self.data_valid),
        )
        assert response.status_code == 406
        assert response.json == {
            "message": "Output type not acceptable: jpeg",
        }

    @pytest.mark.parametrize("imagetype", ["png", "svg"])
    def test_invalid_no_data(self, client, imagetype):
        response = client.get(
            url_for("wireviz-web._render_plant_uml", imagetype=imagetype, encoded=""),
        )
        assert response.status_code == 404
        assert response.json["message"].startswith("The requested URL was not found on the server.")

    @pytest.mark.parametrize("imagetype", ["png", "svg"])
    def test_invalid_raw_data(self, client, imagetype):
        response = client.get(
            url_for("wireviz-web._render_plant_uml", imagetype=imagetype, encoded="foobar"),
        )
        assert response.status_code == 400
        assert response.json == {
            "message": "Unable to decode PlantUML Text Encoding format: Incorrect padding",
        }

    @pytest.mark.parametrize("imagetype", ["png", "svg"])
    def test_invalid_encoded_data(self, client, imagetype):
        response = client.get(
            url_for("wireviz-web._render_plant_uml", imagetype=imagetype, encoded=self.data_invalid),
        )
        assert response.status_code == 400
        assert response.json == {
            "message": "Unable to parse WireViz YAML format: Expected a "
                       "dict as top-level YAML input, but got: <class 'str'>",
        }
