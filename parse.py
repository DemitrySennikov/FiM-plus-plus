from lexer import Token
from token_type import TokenType

def parse():
    pass


class MethodNode:
    def __init__(self, method: Token, args: list):
        self.method = method
        self.args = args
        self.body = list()


class CircleNode:
    def __init__(self, circle_type: TokenType):
        self.type = circle_type
        self.body = list()


class ArgumentNode:
    def __init__(self, name: str, value_type: TokenType, value):
        self.name = name
        self.type = value_type
        self.value = value
