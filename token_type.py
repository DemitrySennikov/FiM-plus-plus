from enum import Enum


class TokenType(Enum):
    IfEnding = 1
    Addition = 2
    Subtraction = 3
    Division = 4
    Than = 5
    Or = 6
    By = 7
    Greater = 8
    LessThanOrEqual = 9
    Less = 10
    NotEqual = 11
    For = 12
    In = 13
    IterEnding = 14
    While = 15
    DoWhileEnding = 16
    Switch = 17
    SwitchNumberEnding = 18
    Hoof = 19
    Default = 20
    GreaterOrEqual = 21
    Either = 22
    Multiplication = 23
    Else = 24
    VariableModifier = 255
    Identifier = 25
    Identifier2 = 256
    ClassDeclaration = 26
    ClassEnding = 27

    MainTag = 28

    MethodDeclaration = 29
    MethodArguments = 30
    MethodReturnType = 31
    MethodEnding = 32

    MethodReturn = 33
    MethodCall = 34

    LeftBracket = 35
    RightBracket = 36
    Punctuation = 37
    NewLine = 38
    Space = 39

    VariableDeclarationStart = 40
    VariableDeclarationMiddle = 41
    VariableConstant = 42
    Nothing = 43

    Article = 44

    NumberType = 45
    CharacterType = 46
    StringType = 47
    BooleanTrue = 48
    BooleanFalse = 49
    BooleanType = 50

    ArrayDeclaration = 51
    NumberArray = 52
    CharacterArray = 53
    StringArray = 54
    BooleanArray = 55

    Quotes = 56

    Apostrophe = 57
    Character = 58

    Increment = 59
    Decrement = 60
    And = 61
    InlineComment = 62
    BlockComment = 63
    String = 64
    Input = 65
    Print = 66

    If = 67

    Not = 68
    Then = 69
    Number = 70
    From = 71
