learn spacy : https://spacy.pythonhumanities.com

## 1. Using SpaCy’s EntityRuler

### 1.1. Key Concepts in this Notebook¶
* pipe
* factory
* EntityRuler
* PhraseMatcher
* Matcher

### 1.2. Introduction to Spacy’s EntityRuler¶
The Python library spaCy offers a few different methods for performing rules-based NER. One such method is via its EntityRuler.

The EntityRuler is a spaCy factory that allows one to create a set of patterns with corresponding labels. A factory in spaCy is a set of classes and functions preloaded in spaCy that perform set tasks. In the case of the EntityRuler, the factory at hand allows the user to create an EntityRuler, give it a set of instructions, and then use this instructions to find and label entities.

Once the user has created the EntityRuler and given it a set of instructions, the user can then add it to the spaCy pipeline as a new pipe. I have spoken in the past notebooks briefly about pipes, but perhaps it is good to address them in more detail here.

A pipe is a component of a pipeline. A pipeline’s purpose is to take input data, perform some sort of operations on that input data, and then output those operations either as a new data or extracted metadata. A pipe is an individual component of a pipeline. In the case of spaCy, there are a few different pipes that perform different tasks. The tokenizer, tokenizes the text into individual tokens; the parser, parses the text, and the NER identifies entities and labels them accordingly. All of this data is stored in the Doc object as we saw in Notebook 01_01 of this series.

It is important to remember that pipelines are sequential. This means that components earlier in a pipeline affect what later components receive. Sometimes this sequence is essential, meaning later pipes depend on earlier pipes. At other times, this sequence is not essential, meaning later pipes can function without earlier pipes. It is important to keep this in mind as you create custom spaCy models (or any pipeline for that matter).

In this notebook, we will be looking closely at the EntityRuler as a component of a spaCy model’s pipeline. Off-the-shelf spaCy models come preloaded with an NER model; they do not, however, come with an EntityRuler. In order to incorperate an EntityRuler into a spaCy model, it must be created as a new pipe, given instructions, and then added to the model. Once this is complete, the user can save that new model with the EntityRuler to the disk.

The full documentation of spaCy EntityRuler can be found here: https://spacy.io/api/entityruler .

This notebook with synthesize this documentation for non-specialists and provide some examples of it in action.

### 1.3. Demonstration of EntityRuler in Action¶
In the code below, we will introduce a new pipe into spaCy’s off-the-shelf small English model. The purpose of this EntityRuler will be to identify small villages in Poland correctly






```
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

```