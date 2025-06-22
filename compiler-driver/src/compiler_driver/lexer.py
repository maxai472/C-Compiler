import sys
from pathlib import Path
import re



def lex(filePath):
# 1. Declare regex patterns of types, order from longest to shortest
# 2. Create a combined regex with groups
# 3. Load file content
# 4. Remove preceding whitespace
# 5. Match against compiled regex
# 6. Add to 'tok
    tokens = [
        ('INT', r'int\b'),
        ('VOID', r'void\b'),
        ('RETURN', r'return\b'),
        ('CONST', r'[0-9]+\b'),
        ('ID', r'[a-zA-Z_]\w*\b'),
        ('LPAREN', r'\('),
        ('RPAREN', r'\)'),
        ('LBRACE', r'\{'),
        ('RBRACE', r'\}'),
        ('COMMENT',   r'//[^\n]*'),       # ✅ Single-line comment
        ('MCOMMENT',  r'/\*.*?\*/'),
        ('SEMI', r';'),
        ('WHITESPACE', r'[ \t\n\r]+'),
        ('MISMATCH', r'.'),
    ]

    regex_groups = '|'.join(f'(?P<{name}>{pattern})' for name, pattern in tokens)
    re_compiled = re.compile(regex_groups)

    with open(filePath, 'r') as f:
        file_content = f.read()

    pos = 0;
    tokens = []

    while pos < len(file_content):
        match = re_compiled.match(file_content, pos)
        if not match:
            print('Invalid character, compilation failed')
            sys.exit(1)
        
        kind = match.lastgroup
        value = match.group()

        if kind == 'MISMATCH':
            print(f"Unexpected character: {value!r} at position {pos}", file=sys.stderr)
            sys.exit(1)
        

        if kind == 'COMMENT':
            pos = match.end()
            continue

        if kind != 'WHITESPACE':
            tokens.append((kind, value))

        pos = match.end()

    
    return tokens


print(lex('/home/batman/Documents/Compiler-Project/Test-Files/return_2.c'))




