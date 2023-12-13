class PonyException(Exception):
    def __init__(self, message=""):
        self.message = message
        super().__init__(message)


class PonyValueException(PonyException):
    pass


class LexerError(PonyException):
    def __init__(self, position):
        super().__init__()
        self.position = position
