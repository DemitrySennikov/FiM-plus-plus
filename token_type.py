from enum import Enum


class TokenType(Enum):
    Identifier = 0
    ClassDeclaration = 1
    ClassEnding = 2

    MainTag = 3

    MethodDeclaration = 4
    MethodArguments = 5
    MethodReturnType = 6
    MethodEnding = 6

    MethodReturn = 7
    MethodCall = 8

    LeftBracket = 9
    RightBracket = 10
    Punctuation = 11


    NewLine = 13
    Space = 14

    VariableDeclarationStart = 15
    VariableDeclarationMiddle = 16
    VariableConstant = 17
    Nothing = 18

    Article = 19

    NumberType = 20
    CharacterType = 21
    StringType = 22
    BooleanTrue = 23
    BooleanFalse = 50

    ArrayDeclaration = 24
    NumberArray = 25
    CharacterArray = 26
    StringArray = 27
    BooleanArray = 28

    Quotes = 29

    Apostrophe = 30
    Character = 228

    InfixAdditionStart = 31
    InfixAdditionEnd = 32
    InfixSubtractionStart = 33
    InfixSubtractionEnd = 34
    InfixMultiplicationStart = 35
    InfixMultiplicationEnd = 36
    InfixDivisionStart = 37
    InfixDivisionEnd = 38

    PrefixAdditionStart = 39
    PrefixAdditionEnd = 49
    PrefixSubtractionStart = 40
    PrefixSubtractionEnd = 41
    PrefixMultiplicationStart = 42
    PrefixMultiplicationEnd = 43
    PrefixDivisionStart = 44
    PrefixDivisionEnd = 45

    Increment = 46
    Decrement = 47
    And = 48
    InlineComment = 51
    BlockComment = 52
    String = 53
    Input = 54
    Print = 55

    If = 56
    When = 57

    Not = 58
    Then = 59
    Number = 337