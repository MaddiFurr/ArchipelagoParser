import re
import json
class Player:
    spheres =[]
    highest = None

regx = re.compile ('^([^:]+): *(.*?) *$',re.MULTILINE)
with open('sample.txt', 'r') as f:
    lines = f.readlines()
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

with open('dict.txt', 'w') as file:
    file.write(str(dictionary))

