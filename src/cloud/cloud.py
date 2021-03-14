import os
import json
from google.cloud import pubsub_v1
from . import exceptions


class Publisher:
    def __init__(self, topic_id):
        project_id = os.environ['PROJECT_ID']
        self.__publisher = pubsub_v1.PublisherClient()
        self.__topic = topic_id
        self.__project_id = project_id
        self.__topic_path = \
            self.__publisher.topic_path(project_id, topic_id)

    def publish(self, data, tries=2):
        data = json.dumps(data)
        result = None
        i = 0
        while not result and i < tries:
            try:
                result = self.__do_publish(data)
            except RuntimeError as error:
                print(f'Error to publish message: {error}')
                i += 1
        if not result:
            raise exceptions.PublishError(f'Error to publish message to topic: {self.__topic}')
        return result

    def __do_publish(self, data):
        data = data.encode("utf-8")
        future = self.__publisher.publish(self.__topic_path, data)
        return future.result()


class ChallengePlayerPublisher(Publisher):
    def __init__(self):
        topic_id = os.environ['CHL_PLAYER_TOPIC_ID']
        super().__init__(topic_id)
