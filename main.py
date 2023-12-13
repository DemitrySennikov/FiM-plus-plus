import argparse
import os.path

from exceptions import *
from lexer import tokenize

if __name__ == "__main__":
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
            tokens = tokenize(inp)
            for token in tokens:
                print(token)
    except PonyException as e:
        print(e)
    except OSError as e:
        print(e)
    except Exception as e:
        print("Something went wrong.")
        print(e)
