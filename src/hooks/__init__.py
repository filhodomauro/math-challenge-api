from repositories import TaskRepository


def on_insert_matches(matches):
    print('on_insert_matches')
    for match in matches:
        match['status'] = 'PLAYING'
        match['results'] = []


def on_inserted_matches(matches):
    print('on_inserted_matches')
    match = matches[0]
    players = match['players']

    challenge = match['challenge_id']
    tasks = TaskRepository().get_tasks(challenge)

    for player in players:
        post_message(match['_id'], player['id'], tasks)


def post_message(match_id, player_id, tasks):
    print(match_id, player_id, tasks)


__all__ = ['on_insert_matches', 'on_inserted_matches']