


# Spacy Notebook :->
--------------------------------------------------------------------------------------------------------------------------------

Mr. Manish kumar 
- April 2024


## 1. The Basics of spaCy
* In this notebook, we will not be working with spaCy in code, rather in concept. This entire JupyterBook is designed around approaching spaCy top-down. By this I mean approaching the things that spaCy does and can do and then exploring how to implement that in code. I think this is necessary so that as you explore the smaller components of spaCy, such as the Lemmatizer, you will understand how it fits into the larger architecture of the spaCy framework.

###  1.1 What is spaCy ?

* A good way to begin is by exploring the question, “What is spaCy?” spaCy (yes, spelled with a lowercase “s” and uppercase “C” is a natural language processing framework. Natural language processing, or NLP, is a branch of linguistics that seeks to parse human language in a computer system. This field is generally referred to as computational linguistics, though it has far reaching applications beyond academic linguistic research.

* NLP is used in every sector of industry, from academics who leverage it to aid in research to financial analysts who try and predict the stock market. Lawyers use NLP to help analyze thousands of legal documents in seconds to target their research and medical doctors use it to parse patient charts. NLP has been around for decades, but with the increased promise of deep learning, a subfield of machine learning, that NLP rapidly expanded. This is because, as we shall learn all too well throughout this book, language is inherently ambiguous. By this, I mean that language does not always make perfect sense. In some cases, it is entirely illogical. The double-negative in English is a good example of this. In some contexts, it can be an emphatic positive, as in, “I cannot stress this enough, I do not like pasta.” This is, of course a lie. I love pasta, but you get my point. In other cases, the double negative can be an emphatic negative, as in, “I ain’t not doing that!”

* As humans, especially native speakers of a language, we can parse these complex illogical statements with ease, especially with enough context. For computers, this is not always easy.

* Because NLP is such a complex problem for computers, it requires a complex solution. The answer has been found in artificial neural networks, or ANNs or neural nets for short. These are the primary areas of research for deep learning practitioners. As the field of deep learning (and machine learning in general) expand and advance, so too does NLP. New methods for training, such as transformer models, push the field further.


### 1.2 How to install spaCy

```
nlp = spacy.load('en_core_web_sm')
# other wise 
nlp = spacy.load(r'C:\Users\Mandhata Kumar\AppData\Local\Programs\Python\Python312\Lib\site-packages\en_core_web_sm\en_core_web_sm-3.7.1')
```
Excellent! spaCy is now installed correctly and we have successfully downloaded the small English model. We will pick up here with the code in the next notebook. For now, I want to focus on big-picture items, specifically spaCy “containers”.

### 1.3 Container 
Containers are spaCy objects that contain a large quantity of data about a text. When we analyze texts with the spaCy framework, we create different container objects to do that. Here is a full list of all spaCy containers. We will be focusing on three (emboldened): Doc, Span, and Token.

* **Doc**
* DocBin
* Example 
* Language 
* Lexeme 
* **Span**
* SpanGroup 
* **Token**

I created the image below to show how I visualize spaCy containers in my mind. At the top, we have a Doc container. This is the basis for all spaCy. It is the main object that we create. Within the Doc container are many different attributes and subcontainers. One attribute is the Doc.sents, which contains all the sentences in the Doc container. The doc container (and each sentence generator) is made up of a set of token containers. These are things like words, punctuation, etc.

Span containers are kind of like token, in that they are a piece of a Doc container. Spans have one thing that makes them unique. They can cross multiple tokens.

We can give spans a bit more specificity by classifying them into different groups. These are known as SpanGroup containers.

![alt text](Image/spacy_containers.png)


## 2. Getting Started with spaCy and its Linguistic Annotations
i was write the code [This notebook]("https://github.com/ProgramerSalar/spaCy/blob/manish/notebook/00_spaCy_and_its_Linguistic_Annotations.py")


In this chapter, we will start working with spaCy directly. The goals of this chapter are twofold. First, it is my hope that you understand the basic spaCy syntax for creating a Doc container and how to call specific attributes of that container. Second, it is my hope that you leave this chapter with a basic understanding of the vast linguistic annotations available in spaCy. While we will not explore all attributes, we will deal with many of the most important ones, such as lemmas, parts-of-speech, and named entities. By the time you are finished with this chapter, you should have enough of a basic understanding of spaCy to begin applying it to your own texts.

### 2.1 Importing Spacy and Loading Data 
```
import spacy
nlp = spacy.load("en_core_web_sm")
with open("F:\spaCy-master\data\hp.txt", "r") as f:
    text = f.read()
    print(text)
```

### 2.2 Creating a Doc Container 
with the data loaded in it's time to make our Doc container. Unless you are working with multiple Doc containers. it is best practice to always call this object 'doc', all lowercase. To create a doc container, we will usually just call our nlp object and padd our text to it as single argument. 

```
doc = nlp(text)
print(doc)
``` 
output: 
```
The United States of America (U.S.A. or USA), commonly known as the United States (U.S. or US) or America, is a country primarily located in North America. It consists of 50 states, a federal district, five major unincorporated territories, 326 Indian reservations, and some minor possessions.[j] At 3.8 million square miles (9.8 million square kilometers), it is the world's third- or fourth-largest country by total area.[d] The United States shares significant land borders with Canada to the north and Mexico to the south, as well as limited maritime borders with the Bahamas, Cuba, and Russia.[22] With a population of more than 331 million people, it is the third most populous country in the world. The national capital is Washington, D.C., and the most populous city is New York.

Paleo-Indians migrated from Siberia to the North American mainland at least 12,000 years ago, and European colonization began in the 16th century. The United States emerged from the thirteen British colonies established along the East Coast. Disputes over taxation and political representation with Great Britain led to the American Revolutionary War (1775â€“1783), which established independence. In the late 18th century, the U.S. began expanding across North America, gradually obtaining new territories, sometimes through war, frequently displacing Native Americans, and admitting new states; by 1848, the United States spanned the continent. Slavery was legal in the southern United States until the second half of the 19th century when the American Civil War led to its abolition. The Spanishâ€“American War and World War I established the U.S. as a world power, a status confirmed by the outcome of World War II.

During the Cold War, the United States fought the Korean War and the Vietnam War but avoided direct military conflict with the Soviet Union. The two superpowers competed in the Space Race, culminating in the 1969 spaceflight that first landed humans on the Moon. The Soviet Union's dissolution in 1991 ended the Cold War, leaving the United States as the world's sole superpower.

The United States is a federal republic and a representative democracy with three separate branches of government, including a bicameral legislature. It is a founding member of the United Nations, World Bank, International Monetary Fund, Organization of American States, NATO, and other international organizations. It is a permanent member of the United Nations Security Council. Considered a melting pot of cultures and ethnicities, its population has been profoundly shaped by centuries of immigration. The country ranks high in international measures of economic freedom, quality of life, education, and human rights, and has low levels of perceived corruption. However, the country has received criticism concerning inequality related to race, wealth and income, the use of capital punishment, high incarceration rates, and lack of universal health care.
```

if you know that what is the lengeth of of text and what is the lengeht of document -> if you count the length of document then lengeth are decrease compre to the length of text 

```
print(len(text))
print(len(doc))
```
output: 
```
3225
652
```

what is going on here? Same text, but different length. Why does the occur? To answer that let's explore it more deeply and try and print off each item in each object. 
```
for token in text[:10]:  
    print(token)
``` 
output: 
