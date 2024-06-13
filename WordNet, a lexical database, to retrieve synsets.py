import nltk
from nltk.corpus import wordnet as wn
nltk.download('wordnet')
nltk.download('omw-1.4')
def explore_word(word):
    synsets = wn.synsets(word)   
    print(f"Synsets for '{word}':")
    for synset in synsets:
        print(f"\nSynset: {synset.name()}")
        print(f"  Definition: {synset.definition()}")
        print(f"  Examples: {synset.examples()}")
        lemmas = synset.lemmas()
        print("  Lemmas:")
        for lemma in lemmas:
            print(f"    Lemma: {lemma.name()}")
            antonyms = [ant.name() for ant in lemma.antonyms()]
            print(f"    Antonyms: {', '.join(antonyms) if antonyms else 'None'}")
        similar_synsets = synset.similar_tos()
        similar_words = set()
        for similar_synset in similar_synsets:
            similar_words.update(lemma.name() for lemma in similar_synset.lemmas())
        print(f"  Similar words: {', '.join(similar_words) if similar_words else 'None'}")
word = "bank"
explore_word(word)
