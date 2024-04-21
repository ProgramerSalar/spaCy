## Name Entity Recognition :- 

import spacy 
import json 
from spacy.lang.en import English
from spacy.pipeline import EntityRuler
        

# import the data 
def load_data(file):
    # open the file and read encodeing is utf-8
    with open(file, 'r', encoding="utf-8") as f:
        # format data is json 
        data = json.load(f)
    return (data)


def generate_better_characters(file):
    data = load_data(file)
    # print("data", len(data))
    # create a new list in which store the new charater of data 
    new_characters = []
    for item in data:
        new_characters.append(item)  # append data in new list like that new_characters
        # print(new_characters)
        
    for item in data:
        # we will replace the data 
        item = item.replace("The", "").replace("the", "").replace("and", "").replace("And", "")
        # print(item)
        names = item.split(" ")  # split the data using space 
        # print(names)
        
        for name in names:
            name = name.strip()   # strip the space in data -> assume that names are three, three differen name sare arranged in new column 
            # print(name)
            new_characters.append(name)
            # print(new_characters)
            
            
        if "(" in item:
            names = item.split("(")   
            # print(names)
            for name in names:
                name = name.replace(")", "").strip()
                # print(name)
                new_characters.append(name)
                # print(new_characters)
                
        if "," in item:
            names = item.split(",")
            for name in names:
                name = name.replace("and", "").strip()
                if " " in name:
                    new_names = name.split()
                    # print(new_names)
                    for x in new_names:
                        x = x.strip()
                        new_characters.append(x)
                        
                new_characters.append(name)
    # print(len(new_characters))
    # print("new_character", new_characters)
    
    final_characters = []
    titles = ["Dr.", "Professor", "Mr.", "Mrs.", "Ms.", "Miss", "Aunt", "Uncle", "Mr. and Mrs."]
    for character in new_characters:
        if "" != character:
            final_characters.append(character)
            for title in titles:
                titled_char = f"{title} {character}"
                final_characters.append(titled_char)
    # print(len(final_characters))
    final_characters = list(set(final_characters))
    # print(len(final_characters))
    final_characters.sort()   # arrange the character in order wise 
    return (final_characters)
                
    
# Certainly! The create_training_data function appears to be part of a machine learning or natural language processing (NLP) pipeline. Let’s break down what it does:

# Input Parameters:
# file: This parameter likely represents a file (such as a text file or dataset) containing some data.
# type: This parameter specifies the label or category associated with the data. For example, it could be used to indicate whether the data represents positive or negative sentiment, different classes of characters, or any other relevant classification.
# Function Steps:
# The function starts by calling another function called generate_better_characters(file). The purpose of this function is not explicitly clear from the snippet, but it likely processes the data in some way.
# Next, the function initializes an empty list called patterns.
# It then iterates over the data (presumably obtained from generate_better_characters(file)).
# For each item in the data, it creates a dictionary (referred to as a “pattern”) with two keys:
# "label": This key holds the value of the type parameter, which represents the label or category.
# "pattern": This key holds the data item itself.
# The created pattern dictionaries are appended to the patterns list.
# Finally, the function returns the list of patterns.
# Output:
# The function returns a list of dictionaries, where each dictionary contains a label and the corresponding data pattern.

def create_training_data(file, type):
    data = generate_better_characters(file)
    patterns = []
    for item in data:
        # print(item)
        pattern = {
            "label":type,
            "pattern":item
        }
        # print(pattern)
        patterns.append(pattern)
    # print(patterns)
    return (patterns)


def generate_rules(patterns):
    
    # Initialize the English NLP pipeline
    nlp = spacy.blank("en")
    
    # Create an entity ruler with a unique name
    ruler = nlp.add_pipe("entity_ruler", name="entity_ruler")
    
    # Add patterns to the entity ruler
    ruler.add_patterns(patterns)
    
    # Save the entire NLP pipeline (including the entity ruler) to disk
    nlp.to_disk("hp_ner")
    
    


patterns = create_training_data("data\\hp_characters.json", "PERSON")
# # print(a)
generate_rules(patterns)


def test_model(model, text):
    doc = nlp(text)
    results = []
    for ent in doc.ents:
        results.append(ent.text)
    return (results)


nlp = spacy.load("hp_ner")
# print(nlp)

with open("F:\spacy\data\hp.txt", "r") as f:
    # print(f)
    text  = f.read()
    # print(text)
    
    # [1:]: This is a slice operation that takes all elements of the list except for the first one (0 index). 
    chapters = text.split("CHAPTER")[1:]
    # print(chapters)
    for chapter in chapters:
        # print(chapter)
# chapter: This is a string variable that presumably contains text data, which includes a chapter number and a chapter title separated by two newline characters (\n\n).
# .split("\n\n"): This method splits the chapter string into a list of substrings wherever it finds two newline characters. The result is a list where each element is a substring that was separated by "\n\n" in the original string.
# [0:2]: This is a slice operation that takes the first two elements from the list created by the split method. If there are at least two elements in the list, it will take those; otherwise, it will take as many as are available (which could be just one or none).
#  Like "Chapter 1\n\nThe Beginning" --> ["Chapter 1", "The Beginning"]

        chapter_num, chapter_title = chapter.split("\n\n")[0:2]
        # print(chapter_num)
        # print(chapter_title)
        chapter_num = chapter_num.strip()
        # [2:]: This is a slice operation that takes all elements of the list starting from the third element (index 2) to the end. This is used because the first two elements (at index 0 and 1) are usually the chapter number and title, which are not needed if you’re only interested in the content segments themselves.
        segments = chapter.split("\n\n")[2:]
        # print(segments)
        hits = []
        for segment in segments:
            # print(segment)
            segment = segment.strip()
            # print(segment)
            segment = segment.replace("\n", " ")
            # print(segment)
            results = test_model(nlp, segment)
            # print(results)
            for result in results:
                hits.append(result)
                
            # print(hits)
                
        
        
        
        
        


    
