import nltk
from nltk import CFG
grammar = CFG.fromstring("""
    S -> NP VP
    NP -> Det N | 'I'
    VP -> V NP | VP Adv
    Det -> 'the' | 'a'
    N -> 'man' | 'dog' | 'park'
    V -> 'saw' | 'walked'
    Adv -> 'quickly'
""")
def check_agreement(parse_tree):
    if parse_tree.label() == 'S':
        for subtree in parse_tree:
            if subtree.label() == 'NP':
                noun = subtree[1]
            elif subtree.label() == 'VP':
                verb = subtree[0]
        if noun[0] == 'I' and verb[0] in ['saw', 'walked']:
            print("Agreement is correct: 'I' is singular and the verb agrees.")
        elif noun[0] != 'I' and verb[0] in ['saw', 'walked']:
            print("Agreement is correct: Noun is singular and the verb agrees.")
        else:
            print("Agreement is incorrect: Noun and verb do not agree.")
sentence = "the man saw a dog quickly"
parser = nltk.ChartParser(grammar)
for tree in parser.parse(sentence.split()):
    tree.pretty_print()
    check_agreement(tree)
