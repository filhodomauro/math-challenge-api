import requests
from time import time


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
