import nltk
from nltk import PCFG, ViterbiParser
pcfg_gr = PCFG.fromstring("""
    S -> NP VP [1.0]
    NP -> Det N [0.5] | Pronoun [0.3] | 'John' [0.2]
    VP -> V NP [0.7] | VP PP [0.3]
    Det -> 'the' [0.8] | 'a' [0.2]
    N -> 'man' [0.5] | 'dog' [0.3] | 'park' [0.2]
    Pronoun -> 'I' [0.4] | 'he' [0.3] | 'she' [0.3]
    V -> 'saw' [0.6] | 'walked' [0.4]
    PP -> P NP [1.0]
    P -> 'in' [0.6] | 'on' [0.4]
""")
def format_probability(probability):
    return "{:.10f}".format(probability)
def pcfg_parse_sentence(sentence, pcfg_gr):
    parser = ViterbiParser(pcfg_gr)
    parsed_trees = parser.parse(sentence.split())
    for tree in parsed_trees:
        print("Parse tree probability:",format_probability(tree.prob()))
        tree.pretty_print()
sentence = "the man saw a dog in the park"
pcfg_parse_sentence(sentence, pcfg_gr)
