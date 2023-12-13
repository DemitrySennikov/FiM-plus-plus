from token_type import TokenType

PUNCTUATION = ".,!?‽…:"

KEYWORDS = {
    TokenType.ClassDeclaration: ["Dear "],
    TokenType.ClassEnding: ["Your faithful student"],

    TokenType.MainTag: ["Today "],
    TokenType.MethodDeclaration: ["I learned "],
    TokenType.MethodReturnType: ["with", "to get"],
    TokenType.MethodArguments: ["using"],

    TokenType.MethodReturn: ["Then you get "],
    TokenType.MethodEnding: ["That's all about "],

    TokenType.MethodCall: ["I remembered ", "I would "],

    TokenType.VariableDeclarationStart: ["Did you know that "],
    TokenType.VariableDeclarationMiddle: ["is ", "was ", "has ", "had ",
                                          "like ", "likes ", "liked "],
    TokenType.VariableConstant: ["always "],

    TokenType.BooleanTrue: ["yes", "true", "right", "correct"],
    TokenType.BooleanFalse: ["no", "false", "wrong", "incorrect"],

    TokenType.Article: ["a ", "the "],

    TokenType.Quotes: ["\""],

    TokenType.Apostrophe: ["`"],
}
