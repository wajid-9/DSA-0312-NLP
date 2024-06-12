import re
def tokenize(expression):
    token_specification = [
        ('NUMBER',   r'\d+'),      
        ('PLUS',     r'\+'),       
        ('TIMES',    r'\*'),       
        ('LPAREN',   r'\('),       
        ('RPAREN',   r'\)'),       
        ('SKIP',     r'[ \t]+'),   
        ('MISMATCH', r'.'),        
    ]
    tok_regex = '|'.join('(?P<%s>%s)' % pair for pair in token_specification)
    get_token = re.compile(tok_regex).match
    line = expression
    line_pos = 0
    mo = get_token(line)
    while mo is not None:
        kind = mo.lastgroup
        value = mo.group(kind)
        if kind != 'SKIP':
            yield (kind, value)
        line_pos = mo.end()
        mo = get_token(line, line_pos)
    yield ('EOF', '')
class Parser:
    def __init__(self, tokens):
        self.tokens = tokens
        self.current_token = None
        self.next_token()
    def next_token(self):
        self.current_token = self.tokens.pop(0)
    def parse(self):
        return self.expr()
    def expr(self):
        node = self.term()
        while self.current_token[0] == 'PLUS':
            self.next_token()
            node = ('PLUS', node, self.term())
        return node
    def term(self):
        node = self.factor()
        while self.current_token[0] == 'TIMES':
            self.next_token()
            node = ('TIMES', node, self.factor())
        return node
    def factor(self):
        token = self.current_token
        if token[0] == 'NUMBER':
            self.next_token()
            return ('NUMBER', token[1])
        elif token[0] == 'LPAREN':
            self.next_token()
            node = self.expr()
            if self.current_token[0] != 'RPAREN':
                raise RuntimeError("Missing closing parenthesis")
            self.next_token()
            return node
        else:
            raise RuntimeError(f"Unexpected token: {token[0]}")
expression = "3 + 5 * ( 10 + 4 )"
tokens = list(tokenize(expression))
parser = Parser(tokens)
ast = parser.parse()
print(ast)
