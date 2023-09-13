import re
import json
class Player:
    spheres =[]
    highest = None

regx = re.compile ('^([^:]+): *(.*?) *$',re.MULTILINE)
with open('sample.txt', 'r') as f:
    lines = f.readlines()
f.close()
dictionary = {}
for line in lines:
    dictionary.update(regx.findall(line))

print(dictionary["Archipelago Version 0.4.2  -  Seed"])

playercount = int(dictionary["Players"])
players = []
i = 1
while i <= int(playercount):
    players.append(dictionary["Player " + str(i)])
    print("Added : " + dictionary["Player " + str(i)] + " to the list of players")
    i += 1

print(players)
dictionary.clear()

s = [n for n, l in enumerate(lines) if l.startswith('Playthrough')]
starts = s[0]

## the idea here is to find out where each of the phases are eg '1: {'. Iterate through all numbers until there isn't a line with the text of a number
## then add all of those line numbers to a list. then go down each player and find an occurance of their name. Check the line against the list of lines
## for each number and then find out which one is the highest and create the complettion list based on that.

with open('sample.txt', 'r') as f:
    f.seek(starts)
    for line in f:
        print(line)
