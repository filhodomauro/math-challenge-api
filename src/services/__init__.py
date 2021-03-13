import requests
from time import time
from repositories import MatchRepository


class MatchService:
    def __init__(self):
        self.__repository = MatchRepository()

    def add_result(self, match_id, result):
        match = self.__repository.find_by_id(match_id)
        match['results'].append(result)
        if len(match['results']) == len(match['players']):
            match['status'] = 'FINISHED'
            winner = self.check_winner(match['results'])
            match['winner'] = winner
        self.__repository.save(match)

    @staticmethod
    def check_winner(results):
        winner = ''
        higher_score = 0
        for result in results:
            if result['score'] > higher_score:
                higher_score = result['score']
                winner = result['player_id']
        return winner


class Calculator:
    def __init__(self, base_url):
        self.__base_url = base_url
        self.__url = f'{base_url}/calculate'

    def execute(self, task):
        expression = task['challenge']
        begin = time()
        resp = requests.post(self.__url, data={'expression': expression})
        end = time()
        success = False
        if resp.status_code == 200:
            try:
                success = float(resp.json()['result']) == float(task['result'])
            except RuntimeError as error:
                print(error)
        return {
                'success': success,
                'time': int((end - begin) * 1000),
                'task': task['name']
        }


__all__ = ['Calculator', 'MatchService']
