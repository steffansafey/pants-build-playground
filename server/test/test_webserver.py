from unittest import mock

from server.webserver import run_server


def test_run_server():
    """Pretty useless test just to test out pants."""
    with mock.patch("uvicorn.run") as run_mock:
        run_server()
        run_mock.assert_called_once()
