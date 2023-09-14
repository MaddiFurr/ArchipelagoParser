import re
import json
import sys
import time

print("Welcome to Archipeago Spoiler Parser\nParsing File: " + sys.argv[1])
time.sleep(3)


dictionary = {}
players = []
spherelines = []
line_count = 0

class Player:
    spheres =[]
    highest = None

def playerlist(): #Get the list of all the players in the game
    regx = re.compile ('^([^:]+): *(.*?) *$',re.MULTILINE)
    with open(sys.argv[1], 'r') as f:
        lines = f.readlines()
    f.close()
    dictionary = {}
    for line in lines:
        dictionary.update(regx.findall(line))

    print("\n\nGame Seed: " + dictionary["Archipelago Version 0.4.2  -  Seed"] + "\n")

    playercount = int(dictionary["Players"])
    players = []
    i = 1
    while i <= int(playercount):
        players.append(dictionary["Player " + str(i)])
        i += 1
    
    dictionary.clear()
    return players

def sphere_count(): #Get the total number of spheres
    line_count = 0
    with open(sys.argv[1], 'r') as f:
        for ln in f:
            line_count += 1
            if ': {' in ln:
                spherelines.append(line_count)
    return line_count, spherelines


def player_spheres(p,spherelines):
    line_count = 0
    lines = []
    spheres = []
    highestsphere = 0
    cursphere = 1
    with open(sys.argv[1], 'r') as f:
        for ln in f:
            line_count += 1
            search = ln.split(":")
            if p in search[0] and line_count > spherelines[0]:
                lines.append(line_count)
                print("Line Number: " + str(line_count))
            
    f.close()

    i = 0
    for i in range(len(lines)):
        if lines[i] > spherelines[cursphere]:
            i += 1
            highestsphere = cursphere
            cursphere += 1
            if cursphere >= len(spherelines):
                break
            if i > len(lines):
                break
        
            
    print("Highest Sphere: " + str(highestsphere))


                
                    
                        
    pass
## the idea here is to find out where each of the phases are eg '1: {'. Iterate through all numbers until there isn't a line with the text of a number
## then add all of those line numbers to a list. then go down each player and find an occurance of their name. Check the line against the list of lines
## for each number and then find out which one is the highest and create the complettion list based on that.

line_count, spherelines = sphere_count()
players = playerlist()


print("line Count: " + str(line_count))
print('Total Spheres: ' + str(len(spherelines)))

print("\nPlayer List:")
i = 0
for i in range(len(players)):
    print(players[i])


i = 0
for i in range(len(players)):
    print("\n\nFinding Sphere occurrences for player: " + players[i])
    
    player_spheres(players[i],spherelines)
