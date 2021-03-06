import os
from eve.auth import TokenAuth
from flask import abort
import firebase_admin
from firebase_admin import auth
from firebase_admin.exceptions import FirebaseError
from firebase_admin.auth import ExpiredIdTokenError, InvalidIdTokenError


class UserAuth(TokenAuth):

    def __init__(self, test_mode):
        super().__init__()

        if not test_mode:
            firebase_admin.initialize_app()
        self.__test_mode = test_mode

    def check_auth(self, token, allowed_roles, resource, method):
        if not self.__test_mode:
            try:
                return auth.verify_id_token(token)
            except InvalidIdTokenError as error:
                abort(401, str(error))
            except FirebaseError as error:
                abort(401, str(error))
        else:
            if not token:
                abort(401, 'Unauthorized')
            return token


def auth_not_required(endpoint):
    endpoint.auth_not_required = False
    return endpoint


def check_auth_not_required(endpoint, view_function):
    return '|' in endpoint or \
           getattr(view_function, 'auth_not_required', False)
