
import argparse
from pathlib import Path
import sys
from compiler_driver.lexer import lex 
from compiler_driver.parser import parse

def main():
    parser = argparse.ArgumentParser()
    parser.add_argument('filePath')
    parser.add_argument('--lex', action='store_true')
    parser.add_argument('--parse', action='store_true')
    parser.add_argument('--codegen', action='store_true')
    args = parser.parse_args()
    
    
    if not Path(args.filePath).is_file():
        print("Invalid file", file=sys.stderr)
        return 2
    
    try:
        tokens = lex(args.filePath)
    except:
        return 1

    if args.lex:
        # print tokens or do nothing
        return 0

    parsed = parse(tokens) 
    if args.parse:
        return 0
    if args.codegen:
        return 0

    return 1
