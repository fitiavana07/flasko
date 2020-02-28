# -*- coding: utf-8 -*-
from flasko.auth import UserSession
from flasko.user import User


def test_auth_token(get):
    # A user
    user = User().save()

    # The user is connected
    user_session = UserSession(user=user, token="a-random-token").save()

    # The token
    token = user_session.token

    # Check authentication is running properly
    rv = get("/auth/check", headers={"Authorization": f"Token {token}"})
    assert rv.status_code == 200


def test_auth_token_invalid(get):
    # random invalid token
    invalid_token = "98123l;kvjsadf1908fa"

    # Use the token
    rv = get(
        "/auth/check", headers={"Authorization": f"Token {invalid_token}"}
    )

    # Should return "unauthorized"
    assert rv.status_code == 401
