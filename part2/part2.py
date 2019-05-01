import deap

""" Load in regression.txt into 2d array """
inText = open("regression.txt", "r")
inText = inText.read().splitlines()
data = []
for i in range(2, len(inText)):
    data.append(inText[i].split())

