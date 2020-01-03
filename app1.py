import json
from difflib import get_close_matches

data = json.load(open("data.json"))

def translate(word1):
    word1 = word1.lower()
    if word1 in data:
        return data[word1]
    elif len(get_close_matches(word1, data.keys())) > 0:
        yn = input("Did you mean %s instead? Enter Y if yes, or N if no: " % get_close_matches(word1, data.keys())[0])
        if yn == "Y":
            return data[get_close_matches(word1, data.keys())[0]]
        elif yn == "N":
            return "Word does not exist"
        else:
            return "Error, we didn't understand your input"
    else:
        return "error word does not exist"

word = input("Enter word: ")

output = translate(word)

if type(output) == list:
    for item in output:
        print(item)
else:
    print(output)
