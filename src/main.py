from eve import Eve
from flask import request, abort
import os
import auth
from hooks import on_inserted_matches, on_insert_matches
from services import MatchService


if 'PORT' in os.environ:
    port = int(os.environ.get('PORT'))
    # use '0.0.0.0' to ensure your REST API is reachable from all your
    # network (and not only your computer).
    host = '0.0.0.0'
else:
    port = 5000
    host = '127.0.0.1'

test_mode = 'EXEC_ENV' not in os.environ or os.environ['EXEC_ENV'] == 'PRODUCTION'
user_auth = auth.UserAuth(test_mode)
app = Eve(auth=user_auth)
app.on_insert_matches += on_insert_matches
app.on_inserted_matches += on_inserted_matches


@app.before_request
def login_required():
    if request.endpoint:
        if auth.check_auth_not_required(request.endpoint, app.view_functions[request.endpoint]):
            return

        try:
            if not user_auth.authorized([], None, request.method):
                raise RuntimeError('Unauthorized')
        except Exception as error:
            abort(
                401,
                str(error),
                www_authenticate=("WWW-Authenticate", 'Bearer realm=Pipa"'),
            )


@app.route('/result/<match_id>', methods=['POST'])
def add_result(match_id):
    result = request.get_json()
    MatchService().add_result(match_id, result)
    return "ack"


if __name__ == '__main__':
    app.run(host=host, port=port)


