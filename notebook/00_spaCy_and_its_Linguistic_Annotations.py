import spacy
nlp = spacy.load("en_core_web_sm")
# print(nlp)
with open("F:\spaCy-master\data\hp.txt", "r") as f:
    # print(f)
    text = f.read()
    # print(text)


doc = nlp(text)
# print(doc)

print(len(text))
print(len(doc))



for token in text[:11]:   # first 11 characters from the text string.
    print(token)


for token in doc[:10]:
    print(token)