# -*- coding: utf-8 -*-
from secrets import token_hex

from flasko.auth import UserSession
from flasko.user import User
from pytest import fixture


@fixture
def auth_token():
    user = User().save()
    user_session = UserSession(user=user, token=token_hex()).save()
    return user_session.token
