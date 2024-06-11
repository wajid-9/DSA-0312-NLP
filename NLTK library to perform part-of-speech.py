import nltk
nltk.download('punkt')
nltk.download('averaged_perceptron_tagger')
text = "In a galaxy far far away, there was a small planet. On this small planet, there were many different species."
words = nltk.word_tokenize(text)
pos_tags = nltk.pos_tag(words)
for word, tag in pos_tags:
    print(f"{word}: {tag}")
