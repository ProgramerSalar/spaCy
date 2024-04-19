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


# a = load_data('F:\spacy\data\hp_characters.json')
# print(a)
