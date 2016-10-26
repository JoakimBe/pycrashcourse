import random

##split. Split using a specific delimiter. Split returns a list. By default, space is the delimiter.
# aListOfWords = "Detta är en sträng".split(" ")
#
# for word in aListOfWords:
#     print(word)

##len. len is used to count the lenght of strings, lists, objects etc..
# print(len("Detta är en sträng"))
# print(len(["Detta", "är", "en", "sträng"]))
# print(len({'key1': '1', 'key2': '2'}))

##User input
# userInput = input("Enter your name")
# print(userInput)

##Random number
# number = random.randint(1, 20)
# print(number)

##Regex example
# import re
# isAMatch = re.match("^[0-9]*$", "10d")
# if isAMatch:
#     print("is a match!")
# else:
#     print("not a match :(")

##Run OS commands
# import os

## Print windows routing table
# os.system('route print')

## Clear terminal cross-platform example
# os.system('cls' if os.name == 'nt' else 'clear')

##Exception handling example
# notAnInt = "1"
# try:
#     int(notAnInt)
#     print("Converted the string to an int!")
# except ValueError:
#     print("String is not an int! :(")

##Check if file exist on disk
#import os
#if os.path.exists('game_data.json'):
#    print("File exists!")

##Save file with json data to disk
#import json
#jsonData = {'name': 'John', 'surname': 'Doe'}
#with open('game_data.json', 'w') as outfile:
#    json.dump(jsonData, outfile, sort_keys=True, indent=4, ensure_ascii=False)

##Open file from disk
#import json
#with open('game_data.json') as data_file:
#    data = json.load(data_file)
#print(data)
