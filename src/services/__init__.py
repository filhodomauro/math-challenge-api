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


__all__ = ['MatchService']
