import os
from eve.auth import TokenAuth
from flask import abort
import firebase_admin
from firebase_admin import auth, credentials


class UserAuth(TokenAuth):

    def __init__(self, test_mode):
        super().__init__()

        if not test_mode:
            cred = credentials.Certificate(os.path.join(os.path.dirname(__file__), 'resources/serviceAccountKey.json'))
            firebase_admin.initialize_app(cred)
        self.__test_mode = test_mode

    def check_auth(self, token, allowed_roles, resource, method):
        if not self.__test_mode:
            return auth.verify_id_token(token)
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
