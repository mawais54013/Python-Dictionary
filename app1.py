import json

data = json.load(open("data.json"))

def translate(word1):
    return data[word1]

word = input("Enter word: ")

print(translate(word))
