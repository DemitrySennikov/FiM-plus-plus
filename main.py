import argparse
import os.path

from exceptions import *


def main():
    pass


if __name__ == "__main__":
    try:
        parser = argparse.ArgumentParser(prog="FPP")
        parser.add_argument("path", type=argparse.FileType('r',
                                                           encoding='UTF-8'),
                            help="Path to the FPP code file.")
        args = parser.parse_args()
        path = args.path.name
        if os.path.splitext(path)[1] != ".fpp":
            raise PonyValueException("File's extension should be '.fpp'.")
    except PonyException as e:
        print(e)
    except OSError as e:
        print(e)
    except Exception as e:
        print("Something went wrong.")
