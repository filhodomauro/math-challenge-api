from eve import Eve
from calculator import Calculator
from repository import Repository
import os


def on_insert_matches(items):
    print('on_insert_matches')
    player = items[0]['player']
    calculator = Calculator(player['base_url'])

    challenge = items[0]['challenge_id']
    tasks = Repository().get_tasks(challenge)
    results = []
    for task in tasks:
        results.append(calculator.execute(task))
    player['results'] = results


# Heroku support: bind to PORT if defined, otherwise default to 5000.
if 'PORT' in os.environ:
    port = int(os.environ.get('PORT'))
    # use '0.0.0.0' to ensure your REST API is reachable from all your
    # network (and not only your computer).
    host = '0.0.0.0'
else:
    port = 5000
    host = '127.0.0.1'

app = Eve()
app.on_insert_matches += on_insert_matches

if __name__ == '__main__':
    app.run()
