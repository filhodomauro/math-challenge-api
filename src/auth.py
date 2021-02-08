from eve.auth import TokenAuth
import firebase_admin
from firebase_admin import auth, credentials
import os

cred = credentials.Certificate(os.path.join(os.path.dirname(__file__), 'resources/serviceAccountKey.json'))
firebase_admin.initialize_app(cred)


class UserAuth(TokenAuth):

    def check_auth(self, token, allowed_roles, resource, method):
        auth.verify_id_token(token)


def auth_not_required(endpoint):
    endpoint.auth_not_required = False
    return endpoint


def check_auth_not_required(endpoint, view_function):
    return '|' in endpoint or \
           getattr(view_function, 'auth_not_required', False)
