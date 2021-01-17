# Let's just use the local mongod instance. Edit as needed.

# Please note that MONGO_HOST and MONGO_PORT could very well be left
# out as they already default to a bare bones local 'mongod' instance.
MONGO_HOST = 'localhost'
MONGO_PORT = 27017

# Skip this block if your db has no auth. But it really should.
# MONGO_USERNAME = 'admin'
# MONGO_PASSWORD = 'adm'
# Name of the database on which the user can be authenticated,
# needed if --auth mode is enabled.
# MONGO_AUTH_SOURCE = 'math-challenge-db'

MONGO_DBNAME = 'math-challenge-db'

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