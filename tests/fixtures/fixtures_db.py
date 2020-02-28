# -*- coding: utf-8 -*-
from mongoengine import connect, disconnect, get_db
from pytest import fixture


@fixture
def mock_db():
    connect(db="test", host="mongomock://localhost")
    yield


@fixture(autouse=True)
def clean_db():
    yield
    # Drop all data
    db = get_db()
    for collection in db.list_collection_names():
        db.drop_collection(collection)

    # Disconnect to prevent concurrent connection
    disconnect()
