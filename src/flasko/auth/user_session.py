# -*- coding: utf-8 -*-
from mongoengine import Document, ReferenceField, StringField

from ..user import User


class UserSession(Document):
    """User Session document"""

    meta = {"strict": False}

    #: User reference
    user = ReferenceField(User)

    #: Unique token
    token = StringField()

    @classmethod
    def by_token(cls, token: str):
        return cls.objects(token=token).first()
