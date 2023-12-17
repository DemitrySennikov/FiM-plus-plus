from token_type import TokenType

PUNCTUATION = ".,!?‽…:"

KEYWORDS = {
    TokenType.ClassDeclaration: ["Dear"],
    TokenType.ClassEnding: ["Your faithful student"],

    TokenType.MainTag: ["Today"],
    TokenType.MethodDeclaration: ["I learned"],
    TokenType.MethodReturnType: ["with", "to get"],
    TokenType.MethodArguments: ["using"],

    TokenType.MethodReturn: ["Then you get"],
    TokenType.MethodEnding: ["That's all about"],

    TokenType.MethodCall: ["I remembered", "I would"],

    TokenType.VariableDeclarationStart: ["Did you know that"],
    TokenType.VariableDeclarationMiddle: ["is", "was", "has", "had",
                                          "like", "likes", "liked"],
    TokenType.VariableModifier: ["is now", "are now",
                                 "now like", "now likes", "become", "becomes"],
    TokenType.VariableConstant: ["always"],

    TokenType.BooleanTrue: ["yes", "true", "right", "correct"],
    TokenType.BooleanFalse: ["no", "false", "wrong", "incorrect"],

    TokenType.Input: ["I heard", "I asked", "I read"],
    TokenType.Print: ["I said", "I wrote", "I sang"],

    TokenType.If: ["If", "When"],
    TokenType.Then: ["Then", "then"],
    TokenType.Else: ["Otherwise", "Or else"],
    TokenType.IfEnding: ["That's what I would do"],

    TokenType.Addition: ["plus", "added to", "add", "to"],
    TokenType.Increment: ["got one more"],
    TokenType.Subtraction: ["minus", "without", "subtract",
                            "the difference between"],
    TokenType.Decrement: ["got one less"],
    TokenType.Multiplication: ["times", "multiplied with", "multiply"],
    TokenType.Division: ["divided by", "divide"],

    TokenType.Than: ["than", "Than"],

    TokenType.And: ["and"],
    TokenType.Or: ["or"],
    TokenType.Not: ["not", "it’s not the case that"],
    TokenType.By: ["by"],
    TokenType.Either: ["either"],
    TokenType.Article: ["a", "an", "the"],
    TokenType.Nothing: ["nothing"],

    TokenType.GreaterOrEqual: ["no less than", "not less than",
                               "n't less than"],
    TokenType.Greater: ["more than", "greater than"],
    TokenType.LessThanOrEqual: ["no more than", "not more than",
                                "n't more than",
                                "no greater than", "not greater than",
                                "n't greater than"],
    TokenType.Less: ["less than"],
    TokenType.NotEqual: ["n't"],

    TokenType.For: ["For every"],
    TokenType.In: ["in"],
    TokenType.From: ["from"],
    TokenType.IterEnding: ["That's what I did"],

    TokenType.While: ["Here's what I did", "As long as"],
    TokenType.DoWhileEnding: ["I did this while", "I did this as long as"],

    TokenType.Switch: ["In regards to"],
    TokenType.SwitchNumberEnding: ["st", "nd", "rd", "th"],
    TokenType.Hoof: ["hoof"],
    TokenType.Default: ["If all else fails"],

    TokenType.NumberType: ["number"],
    TokenType.BooleanType: ["logic", "argument"],

    TokenType.BooleanArray: ["logics", "arguments"],
    TokenType.NumberArray: ["numbers"],
    TokenType.ArrayDeclaration: ["many"],
    TokenType.CharacterType: ["character", "letter"],
    TokenType.CharacterArray: ["word", "phrase", "sentence", "quote", "name"],
    TokenType.StringArray: ["words", "phrases", "sentences", "quotes",
                            "names"]
}


ALL_KEYWORDS_LIST = []
for keywords in KEYWORDS.values():
    for string in keywords:
        ALL_KEYWORDS_LIST.append(string)


# LONG_KEYWORDS_LIST = []
# SHORT_KEYWORDS_LIST = []
# for keywords in KEYWORDS.values():
#     for string in keywords:
#         splt = list(filter(None, string.split()))
#         if len(splt) > 1:
#             LONG_KEYWORDS_LIST += splt
#         else:
#             SHORT_KEYWORDS_LIST += [splt[0] + " "]

# SHORT_KEYWORDS_LIST += "\" "
# SHORT_KEYWORDS_LIST += "` "
# ALL_KEYWORDS_LIST = LONG_KEYWORDS_LIST + SHORT_KEYWORDS_LIST
