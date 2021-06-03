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

# parse inputs
start = timeit.default_timer()

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
print(budget)
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

def putLamp(row, col):
    if len(lamps) <= 0:
        mapOfRooms[row][col] = 'x'
        lamps.append([row, col])
        #print("first lamp at: ", row, " ", col)
        return costOfBulb
    else:
        nearestLampX = 10
        nearestLampY = 10
        dxL = 0
        dxR = 0
        dy = 0
        flag = True
        while flag:
            if checkBounds(row - dy - 1, col):
                dy += 1
            if checkBounds(row, col + dxR + 1):
                dxR += 1 
            if checkBounds(row, col - dxL - 1):
                dxL += 1

            # upper edge
            for i in range(-dxL, dxR + 1):
                if checkBounds(row + dy, col + i):
                    if mapOfRooms[row + dy][col + i] == 'x':
                        flag = False
                        nearestLampX = col + i
                        nearestLampY = row + dy
                else:
                    break
            # left edge
            for i in range(0, dy + 1):
                if checkBounds(row - i, col - dxL):
                    if mapOfRooms[row - i][col - dxL] == 'x': 
                        flag = False
                        nearestLampX = col - dxL
                        nearestLampY = row - i
                else:
                    break

            # right edge
            for i in range(0, dy + 1):
                if checkBounds(row - i, col + dxR):
                    if mapOfRooms[row - i][col + dxR] == 'x':
                        flag = False
                        nearestLampX = col + dxR
                        nearestLampY = row - i
                else:
                    break

        cost = distance(col, row, nearestLampX, nearestLampY) * costOfCable + costOfBulb
        #print(cost)
        if (budget - cost >= 0):
            putCable(row, col, nearestLampY, nearestLampX)
            cost -= putCable(row, col, nearestLampY, nearestLampX)
            mapOfRooms[row][col] = 'x'
            lamps.append([row, col])
            #print("new lamp at: ", row, " ", col)
            #print(cost)
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
    startX = lamp[0]
    startY = lamp[1]
    for i in range(startY - radius, startY + radius + 1):
        if (i > numOfRow or i < 0):
            break
        for j in range(startX, startX + radius + 1):
            if (j < 0 or j > numOfCol):
                break
            toBeIlluminated = mapOfRooms[j][i]
            if (toBeIlluminated == '#'):
                break
            if not (toBeIlluminated == 'x' or toBeIlluminated == '#' or toBeIlluminated == '-'):
                if (toBeIlluminated == 'a'):
                    mapOfRooms[j][i] = 'i'
                else:
                    if not (toBeIlluminated == 'i'):
                        mapOfRooms[j][i] = 'a'   

def illuminateLeft(lamp):
    startX = lamp[0]
    startY = lamp[1]
    for i in range(startY - radius, startY + radius + 1):
        if (i > numOfRow or i < 0):
            break
        for j in range(startX - 1, startX - radius - 1, -1):
            if (j < 0 or j > numOfCol):
                break
            toBeIlluminated = mapOfRooms[j][i]
            if (toBeIlluminated == '#'):
                break
            if not (toBeIlluminated == 'x' or toBeIlluminated == '#' or toBeIlluminated == '-'):
                if (toBeIlluminated == 'a'):
                    mapOfRooms[j][i] = 'i'
                else:
                    if not (toBeIlluminated == 'i'):
                        mapOfRooms[j][i] = 'a'

def illuminateDown(lamp):
    startX = lamp[0]
    startY = lamp[1]
    for i in range(startX - radius, startX + radius + 1):
        if (i < 0 or i > numOfCol):
            break
        for j in range(startY + 1, startY + radius + 1):
            if (j < 0 or j > numOfRow):
                break
            toBeIlluminated = mapOfRooms[i][j]
            if (toBeIlluminated == '#'):
                break
            if not (toBeIlluminated == 'x' or toBeIlluminated == '#' or toBeIlluminated == '-'):
                if (toBeIlluminated == 'a'):
                    mapOfRooms[i][j] = 'i'
                else:
                    if not (toBeIlluminated == 'i'):
                        mapOfRooms[i][j] = 'a'


def illuminateUp(lamp):
    startX = lamp[0]
    startY = lamp[1]
    for i in range(startX - radius, startX + radius + 1):
        if (i < 0 or i > numOfCol):
            break
        for j in range(startY, startY - radius - 1, -1):
            if (j < 0 or j > numOfRow):
                break
            toBeIlluminated = mapOfRooms[i][j] 
            if (toBeIlluminated == '#'):
                break
            if not (toBeIlluminated == 'x' or toBeIlluminated == '#' or toBeIlluminated == '-'):
                if (toBeIlluminated == 'a'):
                    mapOfRooms[i][j] = 'i'
                else:
                    if not (toBeIlluminated == 'i'):
                        mapOfRooms[i][j] = 'a'


def returnAtoDot(lamp):
    startX = lamp[0] - radius
    startY = lamp[1] - radius
    for i in range(startY, startY + 2*radius + 1):
        if (i < 0 or i > numOfRow):
            break
        for j in range(startX, startX + 2*radius + 1):
            if (j < 0 or j > numOfCol):
                break
            if mapOfRooms[j][i] == 'a':
                mapOfRooms[j][i] = '.'

def illuminate(lamp):
    illuminateLeft(lamp)
    illuminateRight(lamp)
    illuminateUp(lamp)
    illuminateDown(lamp)
    returnAtoDot(lamp)

def isOptimal(row, col, accuracy= 0.8):
    maxIllum = 0

    ## Q1
    maxIllum += checkWall(row, col, row - radius - 1, col - radius - 1)
    ## Q2
    maxIllum += checkWall(row - 1, col + 1, row - radius -1, col + radius + 1)
    ## Q3
    maxIllum += checkWall(row, col, row + radius + 1, col + radius + 1)
    ## Q4
    maxIllum += checkWall(row + 1, col - 1, row + radius+1, col - radius - 1)

    if maxIllum >= L*L*0.8:
        #print(str(row) + ", " + str(col)),
        if (budget > 0):
            cost = putLamp(row, col)
            lamp = lamps[len(lamps) - 1]
            illuminate(lamp)
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
            cost = isOptimal(row, col)
            budget -= cost

stop = timeit.default_timer()

print('Time: ', stop - start) 
print(len(lamps))
print(budget)



# create a new file for the illuminated room
ill = 0
newFile = open(outfilename,"a") 

for row in range(numOfRow):
    line = ''
    for col in range(numOfCol):
        line += mapOfRooms[row][col]
        if mapOfRooms[row][col] == 'i':
            ill = ill + 1
    line+= '\n'
    newFile.write(line)

print("illuminated area: ", ill)
print("num of lamps: ", len(lamps))

f.close()