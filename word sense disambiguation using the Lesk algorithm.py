import nltk
from nltk.corpus import wordnet as wn
from nltk.tokenize import word_tokenize
nltk.download('wordnet')
nltk.download('omw-1.4')
nltk.download('punkt')
def get_synsets(word):
    return wn.synsets(word)
def get_gloss(synset):
    return synset.definition()
def lesk_algorithm(context_sentence, ambiguous_word):
    context = set(word_tokenize(context_sentence))
    synsets = get_synsets(ambiguous_word)   
    if not synsets:
        return None  
    best_sense = synsets[0]
    max_overlap = 0 
    for synset in synsets:
        signature = set(word_tokenize(get_gloss(synset)))
        overlap = len(context.intersection(signature))      
        if overlap > max_overlap:
            max_overlap = overlap
            best_sense = synset          
    return best_sense
context_sentence = "I went to the bank to deposit my money"
ambiguous_word = "bank"
sense = lesk_algorithm(context_sentence, ambiguous_word)
if sense:
    print(f"Best sense: {sense.name()}")
    print(f"Definition: {sense.definition()}")
else:
    print("No sense found.")
