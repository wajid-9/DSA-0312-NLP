import nltk
from nltk.tag import UnigramTagger, RegexpTagger
from nltk.corpus import treebank
nltk.download('treebank')
nltk.download('punkt')
nltk.download('universal_tagset')
train_sents = treebank.tagged_sents(tagset='universal')[:3000]
unigram_tagger = UnigramTagger(train_sents)
patterns = [
    (r'.*ing$', 'VBG'), (r'.*ed$', 'VBD'), (r'.*es$', 'VBZ'), (r'.*ould$', 'MD'),
    (r'.*\'s$', 'POS'), (r'.*s$', 'NNS'), (r'^-?[0-9]+(.[0-9]+)?$', 'CD'), (r'.*', 'NN')
]
regexp_tagger = RegexpTagger(patterns, backoff=unigram_tagger)
sentence = "The quick brown foxes were jumping over the lazy dog's back."
tokens = nltk.word_tokenize(sentence)
initial_tags = regexp_tagger.tag(tokens)
transformed_tags = [(word, 'VBG' if tag == 'NN' and word.endswith('ing') else tag) for word, tag in initial_tags]
print("Initial Tags:", initial_tags)
print("Transformed Tags:", transformed_tags)
