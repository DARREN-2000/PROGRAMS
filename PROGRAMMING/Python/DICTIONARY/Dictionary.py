import json
from fnmatch import translate
from difflib import get_close_matches

data = json.load(open("data.json"))

def translate(word):
    word = word.lower()
    if word in data:
        return data[word]     
    elif word.title() in data:
        return data[word.title()]
    elif word.upper() in data:
        return data[word.upper()]                                    
    else:
        print(" word is invalid")    
 
word = input(" Enter the word to be Searched")
output = translate(word)

if type(output) == list:
    for item in output:
        print(item)
else:
    print(output)

