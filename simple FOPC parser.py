from pyparsing import Word, alphas, alphanums, Literal, Group, Forward, oneOf, ZeroOrMore, infixNotation, opAssoc
identifier = Word(alphas, alphanums)
variable = Word(alphas.lower(), alphanums)
constant = Word(alphas.upper(), alphanums)
predicate = Word(alphas, alphanums)
AND = Literal('AND')
OR = Literal('OR')
NOT = Literal('NOT')
IMPLIES = Literal('IMPLIES')
LPAREN = Literal('(').suppress()
RPAREN = Literal(')').suppress()
expression = Forward()
atom = Group(predicate + LPAREN + Group(ZeroOrMore(variable | constant + ZeroOrMore(','))) + RPAREN)
negation = Group(NOT + expression)
binaryOp = Group(expression + oneOf('AND OR IMPLIES') + expression)
expression <<= atom | negation | binaryOp
samples = [
    "P(A, B)",
    "NOT Q(x)",
    "P(A, B) AND Q(x)",
    "P(A, B) OR Q(x)",
    "NOT P(A, B) IMPLIES Q(x)"
]
for sample in samples:
    result = expression.parseString(sample)
    print(f"Expression: {sample}")
    print(f"Parsed: {result.asList()}\n")
