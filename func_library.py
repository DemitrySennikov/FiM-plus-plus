from enum import Enum


class NodeType(Enum):
    Argument = 0
    MathFunction = 1
    BoolFunction = 2
    StdFunction = 3
    Method = 4


class ArgumentType(Enum):
    Nothing = 0
    Int = 1
    Bool = 2
    Char = 3
    String = 4
    Array = 5


class Math(Enum):
    Inc = 0
    Add = 1
    Dec = 2
    Sub = 3
    Mul = 4
    Div = 5


class Boolean(Enum):
    Not = 0
    And = 1
    Or = 2
    Xor = 3


class Std(Enum):
    Input = 0
    Output = 1
