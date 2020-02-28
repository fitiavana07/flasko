# -*- coding: utf-8 -*-
from flask_json import FlaskJSON
from mongoengine import Document, ReferenceField


def _custom_encoder(o):
    if isinstance(o, Document):
        """Encode a mongoengine document"""
        result = {}
        for f, field in o._fields.items():
            if type(field) is ReferenceField:
                result[f] = str(getattr(o, f).id)
            else:
                result[f] = getattr(o, f)
        return result


class JSONExt(FlaskJSON):
    def init_app(self, app):
        super().init_app(app)
        self.encoder(_custom_encoder)
