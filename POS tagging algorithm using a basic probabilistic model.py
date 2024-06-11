import nltk
from collections import defaultdict, Counter
nltk.download('treebank')
nltk.download('universal_tagset')
nltk.download('punkt')
corpus = nltk.corpus.treebank.tagged_sents(tagset='universal')
word_tag_counts = defaultdict(Counter)
for sentence in corpus:
    for word, tag in sentence:
        word_tag_counts[word.lower()][tag] += 1

most_likely_tag = {word: tags.most_common(1)[0][0] for word, tags in word_tag_counts.items()}
def simple_pos_tagger(sentence):
    tokens = nltk.word_tokenize(sentence.lower())
    return [(word, most_likely_tag.get(word, 'NOUN')) for word in tokens]
sentence = "In a galaxy far far away, there was a small planet."
tagged_sentence = simple_pos_tagger(sentence)
print(tagged_sentence)
