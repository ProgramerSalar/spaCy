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
    # print("data", data)
    # create a new list in which store the new charater of data 
    new_characters = []
    for item in data:
        new_characters.append(item)  # append data in new list like that new_characters
        # print(new_characters)
        
    for item in data:
        # we will replace the data 
        item = item.replace("The", "").replace("the", "").replace("and", "").replace("And", "")
        # print(item)
        names = item.split(" ")
        print(names)
    


generate_better_characters('F:\spacy\data\hp_characters.json')
# print(a)
