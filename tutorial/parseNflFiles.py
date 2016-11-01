#!/usr/bin/python
import json

matchupFile = open('nflMatchups.json', 'r')

list = []

for line in matchupFile:
    if line['matchup'] not in list:
        list.append(line)
        print line['matchup']

matchupFile.close()

size = len(list)
print size

teamFile = open('nflLines.jl', 'r')
lineFile = open('nflLinesActual.jl', 'r')
