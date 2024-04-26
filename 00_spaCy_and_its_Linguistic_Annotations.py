import spacy     


# nlp = spacy.load("en_core_web_sm")
nlp = spacy.load(r'C:\Users\Mandhata Kumar\AppData\Local\Programs\Python\Python312\Lib\site-packages\en_core_web_sm\en_core_web_sm-3.7.1')

with open ("F:\spacy\data\hp.txt", "r") as f:
    text = f.read()
    # print(text)
    
    
## 2.2 create a Doc container 
doc = nlp(text)
# print(doc)
# output: "There are all kinds of courage," said Dumbledore, smiling. "It takes a
# great deal of bravery to stand up to our enemies, but just as much to
# stand up to our friends. I therefore award ten points to Mr. Neville
# Longbottom."

print(len(doc))   # this is the length of document word
print(len(text))  # this is the length of text character 



# print the 10 text character
for token in text[:10]:
    print(token)
    
# print the 10 word character    
for token in doc[:10]:
    print(token)
    
    
    
