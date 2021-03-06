import timeit
import numpy as np
import matplotlib.pyplot as plt
import os

## file input
inpName = input("Enter file name here (test1, test2, test3, test4): ")
print(inpName)
filename = inpName + "/" + inpName + ".txt"
print(filename)
outfilename = inpName + "/out" + inpName + ".txt"
f = open(filename, "r+")
illufilename = inpName + "/illumination" + inpName + ".txt"

# helper functions
def toCharArray(word):
    return [char for char in word]

def distance(x1,y1,x2,y2):
    return abs(x1-x2) + abs(y1-y2)

start = timeit.default_timer()

# parse inputs

firstRow = f.readline().split()
numOfRow = int(firstRow[0])
numOfCol = int(firstRow[1])
radius = int(firstRow[2])
print(numOfRow)
print(numOfCol)

secondRow = f.readline().split()
costOfCable = int(secondRow[0])
costOfBulb = int(secondRow[1])
budget = int(secondRow[2])
thirdRow = f.readline()
print(budget)

L = 2*radius + 1

# create 2D matrix for the room

mapOfRooms = []
for i in range(numOfRow):
    charArray = toCharArray(f.readline())
    mapOfRooms.append(charArray)

lamps = []

def checkBounds(row, col):
    if (row < 0 or row >= numOfRow or col < 0 or col >= numOfCol):
        return False
    else:
        return True

def putCable(startRow, startCol, endRow, endCol):
    discount = 0
    incRow = 1
    incCol = 1
    if (startRow > endRow):
        incRow = -1
    if (startCol > endCol):
        incCol = -1

    for x in range(startCol+incCol, endCol, incCol):
        if mapOfRooms[startRow][x] == '1':
            discount += 1
        if mapOfRooms[startRow][x] != 'x':
            mapOfRooms[startRow][x] = '1'

    for y in range(startRow, endRow+incRow, incRow):
        if mapOfRooms[y][endCol] == '1':
            discount += 1
        if mapOfRooms[y][endCol] != 'x':
            mapOfRooms[y][endCol] = '1'
    return discount

def putLamp(endRow, endCol):
    global budget
    cost = 0
    if len(lamps) <= 0:
        mapOfRooms[endRow][endCol] = 'x'
        lamps.append([endRow, endCol])
        return costOfBulb
    else:
        minDist = numOfCol+numOfRow
        nearestLamp = lamps[0]
        for lamp in lamps:
            dist = distance(endRow, endCol, lamp[0], lamp[1])
            if (dist < minDist):
                nearestLamp = lamp
                minDist = dist

        cost += minDist * costOfCable + costOfBulb
        if (budget - cost >= 0):
            cost -= putCable(endRow, endCol, nearestLamp[0], nearestLamp[1])
            mapOfRooms[endRow][endCol] = 'x'
            lamps.append([endRow, endCol])
            return cost
        else:
            print("no more money")  
            return 0


def checkWall(startRow, startCol, endRow, endCol):
    count = 0
    incRow = 1
    incCol = 1
    if (startRow > endRow):
        incRow = -1
    if (startCol > endCol):
        incCol = -1
    county = 0
    for y in range(startRow, endRow, incRow):
        county+=1
        countx = 0
        for x in range(startCol, endCol, incCol):
            countx+=1
            if (checkBounds(y, x)):
                currentChar = mapOfRooms[y][x]
                if (countx > radius or county > radius):
                    if (currentChar == 'x'):
                        return -10000
                else:
                    if (currentChar == '.'):
                        count += 1
                    elif (currentChar == '#'):
                        count -= 1
                        break
                    elif (currentChar == 'x'):
                        return -L
            else:
                break

    return count

def illuminateRight(lamp):
    startX = lamp[1]
    startY = lamp[0]
    for i in range(startY - radius, startY + radius + 1):
        if (i > numOfRow or i < 0):
            break
        for j in range(startX, startX + radius + 1):
            if (j < 0 or j > numOfCol):
                break
            toBeIlluminated = mapOfRooms[i][j]
            if (toBeIlluminated == '#'):
                break
            if not (toBeIlluminated == 'x' or toBeIlluminated == '#' or toBeIlluminated == '-' or toBeIlluminated == '1'):
                if (toBeIlluminated == 'a'):
                    mapOfRooms[i][j] = 'i'
                else:
                    if not (toBeIlluminated == 'i'):
                        mapOfRooms[i][j] = 'a'   

def illuminateLeft(lamp):
    startX = lamp[1]
    startY = lamp[0]
    for i in range(startY - radius, startY + radius + 1):
        if (i > numOfRow or i < 0):
            break
        for j in range(startX - 1, startX - radius - 1, -1):
            if (j < 0 or j > numOfCol):
                break
            toBeIlluminated = mapOfRooms[i][j]
            if (toBeIlluminated == '#'):
                break
            if not (toBeIlluminated == 'x' or toBeIlluminated == '#' or toBeIlluminated == '-' or toBeIlluminated == '1'):
                if (toBeIlluminated == 'a'):
                    mapOfRooms[i][j] = 'i'
                else:
                    if not (toBeIlluminated == 'i'):
                        mapOfRooms[i][j] = 'a'

def illuminateDown(lamp):
    startX = lamp[1]
    startY = lamp[0]
    for i in range(startX - radius, startX + radius + 1):
        if (i < 0 or i > numOfCol):
            break
        for j in range(startY + 1, startY + radius + 1):
            if (j < 0 or j > numOfRow):
                break
            toBeIlluminated = mapOfRooms[j][i]
            if (toBeIlluminated == '#'):
                break
            if not (toBeIlluminated == 'x' or toBeIlluminated == '#' or toBeIlluminated == '-' or toBeIlluminated == '1'):
                if (toBeIlluminated == 'a'):
                    mapOfRooms[j][i] = 'i'
                else:
                    if not (toBeIlluminated == 'i'):
                        mapOfRooms[j][i] = 'a'
 

def illuminateUp(lamp):
    startX = lamp[1]
    startY = lamp[0]
    for i in range(startX - radius, startX + radius + 1):
        if (i < 0 or i > numOfCol):
            break
        for j in range(startY, startY - radius - 1, -1):
            if (j < 0 or j > numOfRow):
                break
            toBeIlluminated = mapOfRooms[j][i] 
            if (toBeIlluminated == '#'):
                break
            if not (toBeIlluminated == 'x' or toBeIlluminated == '#' or toBeIlluminated == '-' or toBeIlluminated == '1'):
                if (toBeIlluminated == 'a'):
                    mapOfRooms[j][i] = 'i'
                else:
                    if not (toBeIlluminated == 'i'):
                        mapOfRooms[j][i] = 'a'


def returnAtoDot(lamp):
    startX = lamp[1] - radius
    startY = lamp[0] - radius
    for i in range(startY, startY + 2*radius + 1):
        if (i < 0 or i > numOfRow):
            break
        for j in range(startX, startX + 2*radius + 1):
            if (j < 0 or j > numOfCol):
                break
            if mapOfRooms[i][j] == 'a':
                mapOfRooms[i][j] = '.'

def illuminate(lamp):
    illuminateLeft(lamp)
    illuminateRight(lamp)
    illuminateUp(lamp)
    illuminateDown(lamp)
    returnAtoDot(lamp)

def isOptimal(row, col, accuracy = 0.7):
    maxIllum = 0

    ## Q1
    maxIllum += checkWall(row, col, row - radius - 1, col - radius - 1)
    ## Q2
    maxIllum += checkWall(row - 1, col + 1, row - radius -1, col + radius + 1)
    ## Q3
    maxIllum += checkWall(row, col, row + radius + 1, col + radius + 1)
    ## Q4
    maxIllum += checkWall(row + 1, col - 1, row + radius+1, col - radius - 1)

    if maxIllum >= L*L*accuracy:
        #print(str(row) + ", " + str(col)),
        if (budget > 0):
            cost = putLamp(row, col)
            lamp = lamps[len(lamps) - 1]
            illuminate([row, col])
            return cost
    else:
        return 0


## ALGO STARTS
for row in range(numOfRow):
    for col in range(numOfCol):
        if budget <= 0 or budget <= costOfBulb or budget <= costOfCable:
            break

        if all(x == '#' or x == '-' for x in mapOfRooms[row]) and row < numOfRow - 1:
            if checkBounds(row+1, col):
                row += 1

        currentChar = mapOfRooms[row][col]
        if currentChar == '.':
            budget -= isOptimal(row, col)


accuracy = 0.8
while budget >= costOfCable and budget >= costOfBulb and accuracy > 0:
    accuracy -= 0.1
    if accuracy < 0.1:
        break
    for row in range(numOfRow):
        for col in range(numOfCol):
            if mapOfRooms[row][col] == '.':
                if budget <= 0 or budget <= costOfBulb or budget <= costOfCable:
                    break
                else:
                    budget -= isOptimal(row, col, accuracy)
                    #print("here")
                

firstLamp = lamps[0]
startX = firstLamp[0]
startY = firstLamp[1]
while budget > 0:
    currentPlace = mapOfRooms[startX][startY]
    right = mapOfRooms[startX + 1][startY]
    left = mapOfRooms[startX - 1][startY]
    up = mapOfRooms[startX][startY - 1]
    down = mapOfRooms[startX][startY + 1]
    if currentPlace == 'x':
        if (right != '-' or right != '1'):
            startX += 1
        elif (left != '-' or right != '1'):
            startX -= 1
        elif (up != '-' or right != '1'):
            startY -= 1
        elif (down != '-' or right != '1'):
            startY += 1      

    if (budget == costOfCable ):
        budget -= costOfCable
        if (right != '-'):
            mapOfRooms[startX][startY] = '1'
            mapOfRooms[startX + 1][startY] = 'E'
        elif (left != '-'):
            mapOfRooms[startX][startY] = '1'
            mapOfRooms[startX - 1][startY] = 'E'
        elif (up != '-'):
            mapOfRooms[startX][startY] = '1'
            mapOfRooms[startX][startY - 1] = 'E'
        elif (down != '-'):
            mapOfRooms[startX][startY] = '1'
            mapOfRooms[startX][startY + 1] = 'E'
    elif (currentPlace != '-' and currentPlace != '#'):
        budget -= costOfCable
        if (right != '-'):
            mapOfRooms[startX][startY] = '1'
            mapOfRooms[startX + 1][startY] = 'E'
        elif (left != '-'):
            mapOfRooms[startX][startY] = '1'
            mapOfRooms[startX - 1][startY] = 'E'
        elif (up != '-'):
            mapOfRooms[startX][startY] = '1'
            mapOfRooms[startX][startY - 1] = 'E'
        elif (down != '-'):
            mapOfRooms[startX][startY] = '1'
            mapOfRooms[startX][startY + 1] = 'E'


stop = timeit.default_timer()

print('Time: ', stop - start) 
print("Put ", len(lamps), "lamps.")
print("Left budget is:" ,budget)

# create a new file for the illuminated room
ill = 0

newFile = open(outfilename,"a")
illuFile = open(illufilename,"a") 

for row in range(numOfRow):
    line = ''
    illuline = ''
    for col in range(numOfCol):
        if mapOfRooms[row][col] == 'i':
            illuline += 'i'
            line += '.'
            ill = ill + 1
        else:
            if mapOfRooms[row][col] == '1':
                ill = ill + 1
            line += mapOfRooms[row][col]
            illuline += mapOfRooms[row][col]
    line+= '\n'
    illuline+= '\n'
    newFile.write(line)
    illuFile.write(illuline)

print("illuminated area: ", ill)
print("num of lamps: ", len(lamps))
f.close()
newFile.close()
illuFile.close()
print("Illuminated area is: ", ill)


file = illufilename

area = []

with open(file, "r") as f:
    lines = f.readlines()
    for line in lines:
        if line[-1] == "\n":
            line = line[:-1]

        if len(line) <= 1:
            continue

        line = line.lower()
        row = []
        for i in range(len(line)):
            row.append(line[i])
        area.append(row)

vals = {
    '-': [0, 0, 0],
    "#": [255, 0, 0],
    "i": [255, 255, 0],
    "??": [255, 255, 0],
    "I": [255, 255, 0],
    "x": [0, 0, 255],
    "X": [0, 0, 255],
    "1": [255, 255, 255],
    ".": [69, 69, 69],
    "e": [0, 255, 0]
}

mmap = np.zeros((len(area), len(area[0]), 3))

for i in range(len(area)):
    for j in range(len(area[0])):
        mmap[i,j,:] = vals[area[i][j]]

mmap /= 255
#mmap = mmap.transpose((1, 0, 2))

plt.figure(figsize=(20, 16), dpi=80)
plt.imshow(mmap)
plt.savefig(inpName + "/" + inpName + ".png", bbox_inches='tight')