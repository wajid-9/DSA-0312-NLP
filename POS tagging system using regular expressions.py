import nltk
nltk.download('punkt')
patterns = [
    (r'.*ing$', 'VBG'),   
    (r'.*ed$', 'VBD'),   
    (r'.*es$', 'VBZ'),
    (r'.*ould$', 'MD'),
    (r'.*\'s$', 'POS'),
    (r'.*s$', 'NNS'),
    (r'^-?[0-9]+(.[0-9]+)?$', 'CD'),
    (r'.*', 'NN')
]
regexp_tagger = nltk.RegexpTagger(patterns)
sentence = "The quick brown foxes were jumping over the lazy dog's back."
tokens = nltk.word_tokenize(sentence)
tagged_sentence = regexp_tagger.tag(tokens)
print(tagged_sentence)
