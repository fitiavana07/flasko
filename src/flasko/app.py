# -*- coding: utf-8 -*-
from flask import Flask
from flask_json import as_json


def Flasko(name):
    app = Flask(__name__)

    # ----- ROUTES ------
    _set_routes(app)

    # TODO test cors (mock origin .. ) with LOCAL
    _setup_cors(app)

    # default config
    app.config.update(JSON_ADD_STATUS=False,)

    return app


def _set_routes(app):
    @app.route("/", methods=["GET"])
    @as_json
    def index():
        return {"message": "It works."}

    @app.errorhandler(401)
    @as_json
    def error_401(error):
        return {"message": "Unauthorized", "code": "unauthorized"}, 401

    @app.errorhandler(404)
    @as_json
    def error_404(error):
        return (
            {"message": "Resource not found", "code": "resource_not_found"},
            404,
        )

    @app.errorhandler(405)
    @as_json
    def error_405(error):
        return (
            {"message": "Method not allowed", "code": "method_not_allowed"},
            405,
        )

    @app.errorhandler(500)
    @as_json
    def error_500(error):
        return (
            {
                "message": "Internal server error",
                "code": "internal_server_error",
            },
            500,
        )


def _setup_cors(app):
    @app.after_request
    def app_after_request(response):
        if app.config.get("LOCAL"):
            headers = {
                ("Access-Control-Allow-Origin", "*"),
                ("Access-Control-Allow-Headers", "Content-Type,Authorization"),
                (
                    "Access-Control-Allow-Methods",
                    "GET,PUT,POST,DELETE,OPTIONS",
                ),
                ("Access-Control-Expose-Headers", "Content-Disposition"),
            }
        else:
            from flask import request

            origin = request.headers.get("Origin")
            if origin and origin.endswith(app.config.get("BASE_DOMAIN")):
                headers = {
                    ("Access-Control-Allow-Origin", origin),
                    (
                        "Access-Control-Allow-Headers",
                        "Content-Type,Authorization",
                    ),
                    (
                        "Access-Control-Allow-Methods",
                        "GET,PUT,POST,DELETE,OPTIONS",
                    ),
                    ("Access-Control-Expose-Headers", "Content-Disposition"),
                }
            else:
                headers = []

        [response.headers.add(*header) for header in headers]
        return response
