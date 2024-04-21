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
    print("data", len(data))
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
    print(len(new_characters))
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
    print(len(final_characters))
    final_characters.sort()   # arrange the character in order wise 
    return (final_characters)
                
    
                
                        
            
    


generate_better_characters('F:\spacy\data\hp_characters.json')
# print(a)
