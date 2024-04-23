import spacy
nlp = spacy.load("en_core_web_sm")
# print(nlp)
with open("F:\spaCy-master\data\hp.txt", "r") as f:
    # print(f)
    text = f.read()
    # print(text)


doc = nlp(text)
# print(doc)

# print(len(text))
# print(len(doc))



# for token in text[:11]:   # first 11 characters from the text string.
#     print(token)


# for token in doc[:10]:
#     print(token)


# for teken in text.split()[:10]:
#     print(token)

# word = text.split()[:10]
# i = 5 
# for token in doc[i:8]:
#     print(f"spacy Token {i}: \n {token}\n word split{i}: \n {word[i]} \n\n")


# for sent in doc.sents:
#     print(sent)
#     print(sent[0])


# sentence1 = doc.sents[0]
# print(sentence1)
# The error TypeError: 'generator' object is not subscriptable occurs because doc.sents in spaCy is a generator, and you cannot access elements of a generator using indexing like you would with a list. To fix this error, you can convert the generator to a list first and then access its elements by inde


sentence1 = list(doc.sents)[0]
# print(sentence1)



token2 = sentence1[0]
# print(token2)

# text 
text = token2.text
# print(text)

# Head 
head = token2.head
# print(head)

# Left Edge 
left_edge = token2.left_edge
print(left_edge)


# right edge 
right_edte = token2.right_edge
print(right_edte)

# Entity Type 
entity_type = token2.ent_type
print(entity_type)
