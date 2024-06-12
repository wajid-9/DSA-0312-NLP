import nltk
from nltk import CFG
grammar = CFG.fromstring("""
    S -> NP VP
    NP -> Det N | 'I'
    VP -> V NP | VP Adv
    Det -> 'the' | 'a'
    N -> 'man' | 'dog' | 'park'
    V -> 'saw' | 'walked' |
    Adv -> 'quickly'
""")
def generate_parse_tree(sentence, grammar):
    parser = nltk.ChartParser(grammar)
    try:
        for tree in parser.parse(sentence.split()):
            tree.pretty_print()
            return True
    except ValueError:
        print("No parse tree found.")
        return False
sentence = "the man saw a dog quickly "
generate_parse_tree(sentence, grammar)
