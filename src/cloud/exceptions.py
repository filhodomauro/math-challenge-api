class PublishError(RuntimeError):
    def __init__(self, message):
        super().__init__()
        self.__message = message

    @property
    def get_message(self):
        return self.__message

    def __str__(self):
        return self.__message
