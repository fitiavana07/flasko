# -*- coding: utf-8 -*-
def test_app(client):
    rv = client.get("/")
    assert rv.status_code == 200

    # status_code is not sent
    assert rv.json.get("status") is None


def test_app_error_404(client):
    rv = client.get("/not_found")
    assert rv.status_code == 404
    assert "Resource not found" in rv.json.get("message")
    assert rv.json.get("code") == "resource_not_found"


def test_app_error_405(client):
    app = client.application

    @app.route("/post_only", methods=["POST"])
    def post_only():
        return None

    rv = client.get("/post_only")
    assert rv.status_code == 405
