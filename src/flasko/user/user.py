# -*- coding: utf-8 -*-
from mongoengine import Document


class User(Document):
    """User document.

    Used only to check access token.
    This class should not be used to create a user,
    except for testing.
    """

    meta = {"strict": False}

    def get_id(self):
        return str(self.id)

    @property
    def is_authenticated(self):
        return True

    @property
    def is_active(self):
        return True

    @property
    def is_anonymous(self):
        return False
