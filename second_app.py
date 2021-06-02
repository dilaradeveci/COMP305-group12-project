import timeit

## file input
inpName = input("Enter file name here (test1, test2, test3, test4): ")
print(inpName)
filename = inpName + "/" + inpName + ".txt"
print(filename)
outfilename = inpName + "/out" + inpName + ".txt"
f = open(filename, "r+")

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
        mapOfRooms[row][col] = 'x'
        lamps.append([row, col])
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
            budget -= cost
            mapOfRooms[row][col] = 'x'
            lamps.append([row, col])
        else:
            print("no more money")  


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


def isOptimal(row, col):
    maxIllum = 0

    ## Q1
    maxIllum += checkWall(row, col, row- 2 * radius -1, col- 2 * radius-1)
    ## Q2
    maxIllum += checkWall(row - 1, col + 1, row - 2 * radius -1, col+ 2 * radius+1)
    ## Q3
    maxIllum += checkWall(row, col, row+ 2 * radius+1, col+ 2 * radius+1)
    ## Q4
    maxIllum += checkWall(row + 1, col - 1, row+ 2 * radius+1, col- 2 * radius-1)

    if maxIllum >= L*L*0.8:
        #print(str(row) + ", " + str(col)),
        if (budget > 0):
            putLamp(row, col)
            return True
    else:
        return False


## ALGO STARTS
for row in range(numOfRow):
    for col in range(numOfCol):
        if budget <= 0:
            break

        if all(x == '#' or x == '-' for x in mapOfRooms[row]) and row < numOfRow - 1:
            if checkBounds(row+1, col):
                row += 1

        currentChar = mapOfRooms[row][col]
        if currentChar == '.':
            isOptimal(row, col)

stop = timeit.default_timer()

print('Time: ', stop - start) 
print(len(lamps))
print(budget)

# create a new file for the illuminated room

newFile = open(outfilename,"a") 

for row in range(numOfRow):
    line = ''
    for col in range(numOfCol):
        line += mapOfRooms[row][col]
    line+= '\n'
    newFile.write(line)

f.close()


