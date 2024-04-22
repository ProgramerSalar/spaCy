# from spacy.matcher import Matcher: This imports the Matcher class from the spaCy library. The Matcher class is used to match sequences of tokens based on patterns you define.
# import spacy: This imports the spaCy library so you can load the NLP model and process text.
# nlp = spacy.load(...): This line loads the English language model from the specified path. The model is necessary for tokenization and other NLP tasks.
# matcher = Matcher(nlp.vocab): This initializes a Matcher object with the vocabulary of the loaded NLP model. The vocabulary contains all the details about known words.
# pattern = [{"LIKE_EMAIL":True}]: This defines a pattern that the Matcher will look for. In this case, the pattern is set to match any token that looks like an email address.
# matcher.add("EMAIL_ADDRESS", [pattern]): This adds the defined pattern to the Matcher under the rule name “EMAIL_ADDRESS”.
# doc = nlp("This is an email address: hello@rahol.com"): This processes the text through the NLP pipeline and creates a Doc object, which is a sequence of tokens that have been processed and have additional properties.
# matches = matcher(doc): This uses the Matcher to find matches in the Doc object. It will return a list of tuples, each representing a match. Each tuple contains an ID for the matched rule, the start index, and the end index of the matched span.
# print(matches): This prints out the matches found by the Matcher. If the pattern is matched, it will print the match ID and the positions of the tokens that matched the pattern.


from spacy.matcher import Matcher
import spacy
# import en_core_web_sm
# nlp = en_core_web_sm.load()
nlp = spacy.load(r'C:\Users\Mandhata Kumar\AppData\Local\Programs\Python\Python312\Lib\site-packages\en_core_web_sm\en_core_web_sm-3.7.1')
# print(nlp)
matcher = Matcher(nlp.vocab)
# print(matcher)
pattern = [{"LIKE_EMAIL":True}]
# print(pattern)
matcher.add("EMAIL_ADDRESS", [pattern])
doc = nlp("This is an email address: hello@rahol.com")
# property(doc)
matches = matcher(doc)
print(matches)

# In the text “This is an email address: hello@rahol.com,” the starting index of 6 and the ending index of 7 refer to the token positions in the Doc object created by spaCy, not the character positions in the string. Here’s how it works:

# When spaCy processes a text, it divides the text into tokens (which can be words, punctuation marks, etc.). Each token is given a unique position number, starting from 0. The Matcher object then looks for patterns within these tokens.

# Let’s tokenize the text to understand the indices better:

# 0    1   2  3     4        5         6
# This is an email address: hello@rahol.com

# In this tokenization:

# “This” is token 0.
# “is” is token 1.
# “an” is token 2.
# “email” is token 3.
# “address:” is token 4.
# “hello@rahol.com” is token 6.
# The pattern {"LIKE_EMAIL": True} is looking for tokens that resemble an email address. In this case, “hello@rahol.com” is recognized as an email address and is token 6 in the Doc object.

# Therefore, the output (16571425990740197027, 6, 7) from the Matcher indicates that:

# The pattern named “EMAIL_ADDRESS” (with the ID 16571425990740197027) matched a pattern in the text.
# The match starts at token position 6, which is “hello@rahol.com”.
# The match ends just before token position 7, which doesn’t exist in this case, indicating the end of the document.
# So, the start index 6 and end index 7 are based on the token positions, not the character positions in the original text.



# 16571425990740197027 ye jo token hai o kaya hai or this token kiska hai 
print(nlp.vocab[matches[0][0]].text)



# print(nlp.vocab[matches[0][1]].text)
# print(nlp.vocab[matches[0][2]].text)
# print(nlp.vocab[matches[0][3]].text)
# print(nlp.vocab[matches[0][4]].text)
# print(nlp.vocab[matches[0][5]].text)
# print(nlp.vocab[matches[0][6]].text)
# print(nlp.vocab[matches[0][7]].text)

print(nlp.vocab[matches[0][0]])



