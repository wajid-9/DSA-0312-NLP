import nltk
from sklearn.feature_extraction.text import TfidfVectorizer
import numpy as np
nltk.download('punkt')
documents = [
    "The cat in the hat disabled the mat.",
    "The quick brown fox jumped over the lazy dog.",
    "A journey of a thousand miles begins with a single step.",
    "To be or not to be, that is the question.",
    "All the world's a stage, and all the men and women merely players."
]
def tokenize_and_stem(text):
    tokens = nltk.word_tokenize(text)
    stems = [nltk.stem.PorterStemmer().stem(token) for token in tokens]
    return stems
vectorizer = TfidfVectorizer(tokenizer=tokenize_and_stem, stop_words='english')
tfidf_matrix = vectorizer.fit_transform(documents)
def compute_tfidf(query, tfidf_matrix, vectorizer):
    query_tfidf = vectorizer.transform([query])
    cosine_similarities = (tfidf_matrix * query_tfidf.T).toarray()
    return cosine_similarities
def rank_documents(query, documents, tfidf_matrix, vectorizer):
    scores = compute_tfidf(query, tfidf_matrix, vectorizer)
    ranked_indices = np.argsort(scores, axis=0)[::-1]
    return ranked_indices
query = "journey of miles"
ranked_indices = rank_documents(query, documents, tfidf_matrix, vectorizer)
print("Query:", query)
print("Ranked Documents:")
for idx in ranked_indices:
    print(documents[idx[0]])
