from func_library import *
from abc import abstractmethod

from func_library import NodeType


class ProgramNode():
    def __init__(self, node_type: NodeType):
        self.node_type = node_type

    @abstractmethod
    def call(self):
        pass


class ArgumentNode(ProgramNode):
    def __init__(self, node_type: NodeType, value_type: ArgumentType,
                 value = None):
        super().__init__(node_type)
        self.type = value_type
        self.value = value

    def call(self):
        return self.value
    

class VariableNode(ProgramNode):
    def __init__(self, node_type: NodeType, name: str):
        super().__init__(node_type)
        self.name = name
    

class MathNode(ProgramNode):
    def __init__(self, node_type: NodeType, operation: Math, 
                 value_1: ProgramNode = None, 
                 value_2: ProgramNode = None):
        super().__init__(node_type)
        self.operation = operation
        self.value_1 = value_1
        self.value_2 = value_2

    def call(self):
        a = self.value_1.call()
        b = self.value_2.call()
        if self.operation == Math.Add:
            return a + b
        if self.operation == Math.Sub:
            return a - b
        if self.operation == Math.Mul:
            return a * b
        if self.operation == Math.Div:
            return a // b
        if self.operation == Math.Inc:
            return a + 1
        if self.operation == Math.Dec:
            return a - 1

    
class BoolNode(ProgramNode):
    def __init__(self, node_type: NodeType, operation: Boolean, 
                 value_1: ProgramNode = None, 
                 value_2: ProgramNode = None):
        super().__init__(node_type)
        self.operation = operation
        self.value_1 = value_1
        self.value_2 = value_2

    def call(self):
        a = self.value_1.call()
        b = self.value_2.call()
        if self.operation == Boolean.And:
            return a and b
        if self.operation == Boolean.Or:
            return a or b
        if self.operation == Boolean.Xor:
            return a != b
        if self.operation == Boolean.Not:
            return not a
        

class StdNode(ProgramNode):
    def __init__(self, node_type: NodeType, func: Std, 
                 value: ProgramNode):
        super().__init__(node_type)
        self.func = func
        self.value = value

    def call(self):
        a = self.value.call()
        if self.func == Std.Input:
            return input()
        if self.func == Std.Output:
            print(a)
            return None


class MethodNode(ProgramNode):
    def __init__(self, node_type: NodeType, name: str,
                 program: list, args: dict):
        super().__init__(node_type)
        self.name = name
        self.program = program
        self.args = args

    def call(self):
        pass
