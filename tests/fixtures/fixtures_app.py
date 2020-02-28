# -*- coding: utf-8 -*-
from os import getenv

from flask_mongoengine import MongoEngine
from flasko import Flasko
from flasko.auth import AuthManager
from flasko.json import JSONExt
from pytest import fixture


def _create_app():
    # TODO refactor this function to have
    #   a function called
    app = Flasko("flasko")
    app.config.update(
        TESTING=getenv("TESTING", False),
        MONGODB_SETTINGS={
            "host": getenv("MONGODB_HOST", "mongodb://127.0.0.1:27017/test")
        },
        LOCAL=getenv("LOCAL"),
        BASE_DOMAIN=getenv("BASE_DOMAIN", ""),
    )

    MongoEngine(app)
    JSONExt(app)
    AuthManager(app)

    return app


@fixture
def client(monkeypatch):
    monkeypatch.setenv("MONGODB_HOST", "mongomock://localhost/test")
    monkeypatch.setenv("TESTING", "true")
    return _create_app().test_client()


@fixture
def post(client):
    def _post(*args, **kwargs):
        return client.post(*args, **kwargs)

    return _post


@fixture
def get(client):
    def _get(*args, **kwargs):
        return client.get(*args, **kwargs)

    return _get
