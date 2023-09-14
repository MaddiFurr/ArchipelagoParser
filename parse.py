import re
import json
import sys
import time
import os

print("Welcome to Archipeago Spoiler Parser\nParsing File: " + sys.argv[1])
time.sleep(3)


dictionary = {}
players = []
spherelines = []
line_count = 0

def playerlist(): #Get the list of all the players in the game
    regx = re.compile ('^([^:]+): *(.*?) *$',re.MULTILINE)
    with open(sys.argv[1], 'r') as f:
        lines = f.readlines()
    f.close()
    dictionary = {}
    for line in lines:
        dictionary.update(regx.findall(line))


    playercount = int(dictionary["Players"])
    players = []
    i = 1
    while i <= int(playercount):
        players.append(dictionary["Player " + str(i)])
        i += 1
    
    dictionary.clear()
    return players

def sphere_count(pts): #Get the total number of spheres
    line_count = 0
    with open(sys.argv[1], 'r') as f:
        for ln in f:
            line_count += 1
            if ': {' in ln and line_count > pts:
                spherelines.append(line_count)
    return line_count, spherelines


def player_spheres(p,spherelns,pts):
    line_count = 0
    ourline = []
    spheres = []
    highestln = 0
    cursphere = 1
    with open(sys.argv[1], 'r') as f:
        for ln in f:
            line_count += 1
            search = ln.split("):")
            
            if p in search[0] and line_count > spherelns[0] and line_count > pts:
                ourline.append(line_count)
                highestln = line_count
                #print("Search 0: " + str(search[0]) + " | LINE: " + str(line_count))
    
    f.close()
    highestsphere = 0
    

    i = 0
    n = 0
    chk = True
    while chk:
        if i >= len(spherelns) -1:
            highestsphere = len(spherelns)
            chk = False
            break   
        if highestln > spherelns[i] and i == len(spherelns) -1:
            i -= 1
            highestsphere = len(spherelns) -1
            chk = False
            break
        if highestln < spherelns[i]:
            i -= 1
            highestsphere = i
            chk = False

        i += 1
    if highestsphere >= len(spherelns) - 1:
        if highestln > spherelns[i]:
            highestsphere = len(spherelns) - 1
        elif highestln < spherelns[i]:
            highestsphere = len(spherelns) - 2
    return highestsphere
                
def find_the_fucking_playthrough():
    line_count = 0
    with open(sys.argv[1], 'r') as f:
        for ln in f:
            line_count += 1
            if 'Playthrough:' in ln:
                return line_count
    


pts = find_the_fucking_playthrough()
lncnt, spherelines = sphere_count(pts)
players = playerlist()

if os.path.isfile(".lines"):
    os.remove(".lines")

i = 0
for i in range(len(players)):
    if players[i] != "Spectator":
        sphere = player_spheres(players[i],spherelines,pts)
        temp = open(".lines", "a")
        temp.write(players[i] + "||" + str(sphere) + "\n")
        temp.close()
        i += 1


ufinish = []
with open(".lines") as f:
    for line in f:
        name, sphere = line.strip().split("||")
        
        ufinish.append((name, int(sphere)))

        finishorder = sorted(ufinish, key=lambda x: x[1], reverse=False)

    print('\n\nPredicted Archipelago Finish Order\n<Completion Position>: ("YMAL NAME", <Finishing Sphere>)\n')
    i = 1
    for item in finishorder:
        print("Position " + str(i) + ": " + str(item))
        i += 1
f.close()
os.remove(".lines")