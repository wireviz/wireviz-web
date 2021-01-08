from unittest import mock

from click.testing import CliRunner

from wireviz_web.cli import run


@mock.patch("wireviz_web.Flask", autospec=True)
def test_cli_default(app_mock: mock.MagicMock):

    runner = CliRunner()
    result = runner.invoke(run)
    assert result.exit_code == 0

    assert (
        mock.call().register_blueprint(mock.ANY, url_prefix="") in app_mock.mock_calls
    )
    assert (
        mock.call().run(host="localhost", port=3005, debug=False) in app_mock.mock_calls
    )


@mock.patch("wireviz_web.Flask", autospec=True)
def test_cli_with_url(app_mock: mock.MagicMock):

    runner = CliRunner()
    result = runner.invoke(run, ["--url=/foobar"])
    assert result.exit_code == 0

    assert (
        mock.call().register_blueprint(mock.ANY, url_prefix="/foobar")
        in app_mock.mock_calls
    )


@mock.patch("wireviz_web.Flask", autospec=True)
def test_cli_with_listen(app_mock: mock.MagicMock):

    runner = CliRunner()
    result = runner.invoke(run, ["--listen=foobar:1234"])
    assert result.exit_code == 0

    assert mock.call().run(host="foobar", port=1234, debug=False) in app_mock.mock_calls


@mock.patch("wireviz_web.Flask", autospec=True)
def test_cli_with_debug(app_mock: mock.MagicMock):

    runner = CliRunner()
    result = runner.invoke(run, ["--debug"])
    assert result.exit_code == 0

    assert (
        mock.call().run(host="localhost", port=3005, debug=True) in app_mock.mock_calls
    )
