from token_type import TokenType
from lexer import Token


class PonyInterface:
    def __init__(self, methods: list[str]):
        self.methods = methods


class PonyMethod:
    def __init__(self):
        pass


class PonyClass:
    def __init__(self, superclass, interfaces: list[PonyInterface], 
                 methods: list):
        self.superclass = None
        if superclass is PonyClass:
            self.superclass = superclass
        self.interfaces = interfaces
        self.methods = methods


Princess_Celestria = PonyClass(None, [], [])
