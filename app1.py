import json
from difflib import get_close_matches

data = json.load(open("data.json"))

def translate(word1):
    word1 = word1.lower()
    if word1 in data:
        return data[word1]
    elif len(get_close_matches(word1, data.keys())) > 0:
        return "Did you mean %s instead?" % get_close_matches(word1, data.keys())[0]
    else:
        return "error word does not exist"

word = input("Enter word: ")

print(translate(word))
