
# Demonstration of EntityRuler in Action¶
# In the code below, we will introduce a new pipe into spaCy’s off-the-shelf small English model. The purpose of this EntityRuler will be to identify small villages in Poland correctly.

import spacy 

# build upon the spacy small model 
nlp = spacy.load(r'C:\Users\Mandhata Kumar\AppData\Local\Programs\Python\Python312\Lib\site-packages\en_core_web_sm\en_core_web_sm-3.7.1')

# simple text 
# text = "The village of Treblinka is in Poland. Treblinka was also an extermination camp."
text = "my village Goraper in India. Goraper are located in Bihar"
# create the Doc object 
doc = nlp(text)

# extract entities 
for ent in doc.ents:
    print(ent.text, ent.label_)