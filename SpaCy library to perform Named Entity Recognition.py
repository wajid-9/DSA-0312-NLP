import spacy
nlp = spacy.load("en_core_web_sm")
def perform_ner(text):
    doc = nlp(text)
    for ent in doc.ents:
        print(ent.text, ent.label_)
text = "Apple is looking at buying U.K. startup for $1 billion. Elon Musk founded SpaceX in 2002 in California."
perform_ner(text)
