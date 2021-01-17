import os

MONGO_URI = os.environ.get('MONGODB_URI', 'mongodb://localhost:27017/math-challenge-db')


challenge_schema = {
    # Schema definition, based on Cerberus grammar. Check the Cerberus project
    # (https://github.com/pyeve/cerberus) for details.
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
    'player': {
        'type': 'dict',
        'schema': {
            'name': {
                'type': 'string',
                'required': True,
            },
            'base_url': {
                'type': 'string',
                'required': True
            }
        }
    }
}

match = {
    'item_title': 'matches',
    'resource_methods': ['POST','GET'],
    'schema': match_schema,
}

DOMAIN = {
    'challenges': challenge,
    'matches': match
}