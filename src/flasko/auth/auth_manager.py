# -*- coding: utf-8 -*-
from flask import make_response
from flask_login import LoginManager, login_required

from .user_session import UserSession


def _load_user_from_request(request):
    """Loads the connected user given a token in the header.

    The request must have an Authorization header in the following form:
    Basic token_askjs
    """
    header_value = request.headers.get("Authorization")

    if not header_value:
        return None

    token = header_value.replace("Token ", "", 1)

    user_session = UserSession.by_token(token)
    if not user_session:
        return None

    return user_session.user


@login_required
def _view_test():
    return make_response({})


class AuthManager(LoginManager):
    def init_app(self, app, add_context_processor=True):
        super().init_app(app, add_context_processor)
        self.request_loader(_load_user_from_request)
        self._register_test_view(app)

    def _register_test_view(self, app):
        app.add_url_rule(
            "/auth/check", "auth_check", _view_test, methods=["GET"]
        )
