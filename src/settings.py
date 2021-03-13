import os

MONGO_URI = os.environ.get('MONGODB_URI', 'mongodb://localhost:27017/math-challenge-db')


challenge_schema = {
    'id': {
        'type': 'integer',
        'required': True,
        'unique': True,
    },
    'name': {
        'type': 'string',
        'minlength': 1,
        'maxlength': 20,
        'required': True
    },
    'level': {
        'type': 'list',
        'allowed': ["easy", "medium", "hard"],
    }
}

challenge = {
    'item_title': 'challenges',
    'schema': challenge_schema,
}

match_schema = {
    'challenge_id': {
        'type': 'integer',
        'required': True,
    },
    'players': {
        'type': 'list',
        'schema': {
            'type': 'dict',
            'schema': {
                'id': {
                    'type': 'string',
                    'required': True,
                },
                'name': {
                    'type': 'string',
                    'required': True,
                },
                'base_url': {
                    'type': 'string',
                    'required': True
                },
            }
        }
    },
    'status': {
        'type': 'list',
        'allowed': ['PLAYING', 'FINISHED']
    },
    'results': {
        'type': 'list',
        'schema': {
            'type': 'dict',
            'schema': {
                'player_id': {
                    'type': 'string',
                    'required': True,
                },
                'score': {
                    'type': 'integer',
                    'required': True,
                },
                'correct': {
                    'type': 'integer',
                    'required': True,
                },
                'wrong': {
                    'type': 'integer',
                    'required': True,
                },
                'execution_time': {
                    'type': 'integer'
                }
            }
        }
    },
    'winner': {
        'type': 'string'
    }
}

match = {
    'item_title': 'matches',
    'resource_methods': ['POST', 'GET'],
    'item_methods': ['GET'],
    'schema': match_schema,
}

DOMAIN = {
    'challenges': challenge,
    'matches': match
}