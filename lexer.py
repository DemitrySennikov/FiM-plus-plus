import regex as re

from exceptions import LexerError
from grammar import *


class Token:
    def __init__(self, token_type, value, position):
        self.type = token_type
        self.value = value
        self.position = position

    def __str__(self):
        if self.type == TokenType.NewLine:
            self.value = r"\n"
        return f"{self.type} | '{self.value}' | {self.position}"


class Lexer(object):
    def __init__(self, rules):
        self._input = None
        self._position = 0

        i = 1
        regex_parts = []

        self._group_type = {}
        for regex, _token_type in rules:
            group_name = f"GROUP{i}"
            regex_parts.append(f"(?P<{group_name}>{regex})")
            self._group_type[group_name] = _token_type
            i += 1

        self._regex = re.compile('|'.join(regex_parts),
                                 punctuation=list(PUNCTUATION) + ["(", ")"],
                                 keywords=ALL_KEYWORDS_LIST)

    def _get_next_token(self):
        if self._position >= len(self._input):
            return None
        else:
            match_result = self._regex.match(self._input, self._position)
            if match_result:
                self._position = match_result.end()
                return Token(self._group_type[match_result.lastgroup],
                             match_result.group(match_result.lastgroup),
                             self._position)

            raise LexerError(self._position)

    def get_tokens(self, _input):
        _input = _input.replace("“", "\"").replace("”", "\"") \
            .replace("‘", "`").replace("’", "'")
        self._input = _input
        self._position = 0
        while True:
            _token = self._get_next_token()
            print(_token)
            if _token is None:
                break
            yield _token


def tokenize(inp):
    rules = [
        (rf"[{PUNCTUATION}]", TokenType.Punctuation),
    ]

    for _type in KEYWORDS.keys():
        for keyword in KEYWORDS[_type]:
            rules.append((keyword, _type))

    rules.append((" ", TokenType.Space))
    rules.append(("\n", TokenType.NewLine))
    rules.append((r"\(.*?\)", TokenType.BlockComment))
    rules.append((r"(?:P\.)*S\..*(?:\n|\Z)", TokenType.BlockComment))
    rules.append((r"\"\w*?\"", TokenType.String))
    rules.append((r"[\w' ]*\w(?=\L<punctuation>)", TokenType.Identifier))
    rules.append((r"[\w' ]*\w(?= \L<keywords>)", TokenType.Identifier))

    lexer = Lexer(rules)
    tokens = lexer.get_tokens(inp)

    return list(tokens)
