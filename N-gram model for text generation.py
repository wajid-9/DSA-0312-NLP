import random
import nltk
from collections import defaultdict
nltk.download('punkt')
text = """In a galaxy far far away, there was a small planet. On this small planet, there were many different species. Each species had its own unique characteristics. They lived in harmony for many years until one day, a strange spaceship appeared in the sky."""
words = nltk.word_tokenize(text.lower())
bigram_model = defaultdict(list)
for i in range(len(words) - 1):
    bigram_model[words[i]].append(words[i + 1])
def generate_text(model, start_word, num_words):
    current_word = start_word
    text = [current_word]
    for _ in range(num_words - 1):
        next_words = model[current_word]
        if not next_words:
            break
        current_word = random.choice(next_words)
        text.append(current_word)
    return ' '.join(text)
print(generate_text(bigram_model, 'in', 20))
