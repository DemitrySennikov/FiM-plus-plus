class PonyException(Exception):
    def __init__(self, message):
        self.message = message
        super().__init__(message)


class PonyValueException(PonyException):
    pass