from eve import Eve
from calculator import Calculator
from repository import Repository


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


app = Eve()
app.on_insert_matches += on_insert_matches

if __name__ == '__main__':
    app.run()
