from wireviz_web import create_app


def test_app_cors(monkeypatch, caplog):
    monkeypatch.setenv("CORS_ENABLE", "true")
    create_app()
    assert "CORS enabled for all routes" in caplog.messages
