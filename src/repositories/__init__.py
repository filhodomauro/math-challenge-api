from pymongo import MongoClient
from bson.objectid import ObjectId


class Repository:
    def __init__(self):
        self._db = MongoClient().get_database('math-challenge-db')


class TaskRepository(Repository):
    def __init__(self):
        super().__init__()

    def get_tasks(self, challenge_id):
        collection = self._db.get_collection('tasks')
        return collection.find({'challenge_id': challenge_id})


class MatchRepository(Repository):
    def __init__(self):
        super().__init__()

    def find_by_id(self, match_id):
        return self._db.get_collection('matches').find_one({'_id': ObjectId(match_id)})

    def save(self, match):
        return self._db.get_collection('matches').save(match)


__all__ = ['TaskRepository', 'MatchRepository']
