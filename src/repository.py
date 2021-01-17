from pymongo import MongoClient


class Repository:
    def __init__(self):
        self.__db = MongoClient().get_database('math-challenge-db')

    def get_tasks(self, challenge_id):
        collection = self.__db.get_collection('tasks')
        return collection.find({'challenge_id': challenge_id})
