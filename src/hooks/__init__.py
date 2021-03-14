from repositories import TaskRepository
from cloud import cloud

publisher = cloud.ChallengePlayerPublisher()

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
    mapped_tasks = list(map(map_task, tasks))

    for player in players:
        post_message(str(match['_id']), player['id'], player['base_url'], mapped_tasks)


def post_message(match_id, player_id, url, tasks):
    data = {'match_id': match_id, 'player_id': player_id, 'url': url, 'tasks': tasks}
    publisher.publish(data)


def map_task(task):
    return { 'challenge': task['challenge'], 'result': task['result']}


__all__ = ['on_insert_matches', 'on_inserted_matches']