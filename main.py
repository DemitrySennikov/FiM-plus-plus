import argparse
import os.path

from exceptions import *
from lexer import tokenize

if __name__ == "__main__":
    try:
        try:
            parser = argparse.ArgumentParser(prog="FPP")
            parser.add_argument("path", type=argparse.FileType('r'),
                                help="Path to the FPP code file.")
            args = parser.parse_args()
            path = args.path.name
            extension = os.path.splitext(path)[1]
            if extension != ".fpp" and extension != ".txt":
                raise PonyValueException("File's extension should be '.fpp' "
                                         "or '.txt'.")
            with open(path, "r", encoding='utf-8') as f:
                inp = f.read()
        except OSError as err:
            print(err)

        try:
            tokens = tokenize(inp)
            for token in tokens:
                print(token)
        except LexerError as err:
            print(f"Lexer error at pos {err.position}.")
            print(inp[err.position])
            print(inp[err.position-10:err.position+10])
        except PonyValueException as err:
            print(err)
    except Exception as err:
        print("Something went wrong.")
        print(err)
