import nltk
nltk.download('punkt')
nltk.download('averaged_perceptron_tagger')
nltk.download('wordnet')
from nltk.tokenize import word_tokenize
from nltk.stem import WordNetLemmatizer
from nltk.corpus import wordnet
text="Cats are chasing mice in the garden"
words=word_tokenize(text)
lemmatizer=WordNetLemmatizer()
def get_wordnet_pos(tag):
    if tag.startswith('J'):
        return wordnet.ADJ
    elif tag.startswith('V'):
        return wordnet.VERB
    elif tag.startswith('N'):
        return wordnet.NOUN
    elif tag.startswith('R'):
        return wordnet.ADV
    else:
        return wordnet.NOUN
lemmatized_words=[]
for word,pos in nltk.pos_tag(words):
    wordnet_tag=get_wordnet_pos(pos)
    lemma=lemmatizer.lemmatize(word,wordnet_tag)
    lemmatized_words.append(lemma)
print(lemmatized_words)
