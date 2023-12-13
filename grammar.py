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

    TokenType.Input: ["I heard ", "I asked ", "I read "],
    TokenType.Print: ["I said ", "I wrote ", "I sang "]

    # TokenType.Article: ["a ", "the "],
}

LONG_KEYWORDS_LIST = []
SHORT_KEYWORDS_LIST = []
for keywords in KEYWORDS.values():
    for string in keywords:
        splt = list(filter(None, string.split()))
        if len(splt) > 1:
            LONG_KEYWORDS_LIST += splt
        else:
            SHORT_KEYWORDS_LIST += [splt[0] + " "]

# SHORT_KEYWORDS_LIST += "\" "
# SHORT_KEYWORDS_LIST += "` "
print(SHORT_KEYWORDS_LIST)
ALL_KEYWORDS_LIST = LONG_KEYWORDS_LIST + SHORT_KEYWORDS_LIST
