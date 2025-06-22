import sys

class Node:
    pass
# Expreesion
class Expression(Node):
    pass

class Constant(Expression):
    def __init__(self, value):
        self.value = value

# Statement
class Statement(Node):
    pass

class Return(Statement):
    def __init__(self, exp):
        self.exp = exp
# Function
class Function(Node):
    def __init__(self, name: str, statement: Statement):
        self.name = name
        self.statement = statement
# Program
class Program(Node):
    def __init__(self,  function: Function):
        self.function = function


# Write Token Handle class
class Tokens:
    def __init__(self, tokens):
        self.tokens = tokens
        self.pos = 0

    def peek(self):
        if self.pos >= len(self.tokens):
            return('EOF', '')
        return self.tokens[self.pos]

    def take_token(self):
        token = self.peek()
        self.pos += 1
        return token
    
    def expect(self, expected):
        actual_type, actual_value = self.take_token()
        if expected != actual_type:
            raise SyntaxError(f"Expected - {expected}, Recieved - {actual_type}")
        return actual_value


# Program parser
def parse_program(tokens: Tokens):
    function = parse_function(tokens)
    tokens.expect("EOF")
    return Program(function)
# Function Parser
def parse_function(tokens: Tokens):
    tokens.expect("INT")
    Id = parse_identifier(tokens)
    tokens.expect("LPAREN")
    tokens.expect("VOID")
    tokens.expect("RPAREN")
    tokens.expect("LBRACE")
    statement = parse_statement(tokens)
    tokens.expect("RBRACE")
    return Function(Id, statement)

# Statement Parser
def parse_statement(tokens: Tokens):
    tokens.expect("RETURN")
    expression = parse_expression(tokens)
    tokens.expect("SEMI")
    return Return(expression)

# Expression Parser
def parse_expression(tokens: Tokens):
    return parse_int(tokens)

def parse_identifier(tokens):
    return tokens.expect("ID")

def parse_int(tokens):
    value = tokens.expect("CONST")
    return Constant(int(value))


def parse(input):
    tokens = Tokens(input)
    return parse_program(tokens)
