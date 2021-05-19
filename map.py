
def toCharArray(word):
    return [char for char in word]


f = open("test2.txt", "r+")

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

def putLamp(row, col):
    mapOfRooms[row][col] = 'x'
    lamps.append([row, col])


def manhattanDistance(x1, y1, x2, y2):
    return abs(x1-x2) + abs(y1-y2)

def isLampExistAround(row, col):
    for lamp in lamps:
        if manhattanDistance(row, lamp[0], col, lamp[1]) < L:
            print(str(row) + ", " + str(col))
            print("yaay lamp is found")
            return True
    
    return False

    
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
                if (countx > radius or county > radius):
                    if (currentChar == 'x'):
                        print('heyo')
                        return -10000
                else:
                    currentChar = mapOfRooms[y][x]
                    if (currentChar == '.'):
                        count += 1
                    elif (currentChar == '#'):
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
        #print(str(row) + ", " + str(col))

        putLamp(row, col)
        return True
    else:
        return False


## ALGO STARTS
for row in range(numOfRow):
    for col in range(numOfCol):
        if all(x == '#' or x == '-' for x in mapOfRooms[row]) and row < numOfRow - 1:
            if checkBounds(row+1, col):
                row += 1

        currentChar = mapOfRooms[row][col]
        if currentChar == '.':
            isOptimal(row, col)

newFile = open("out2.txt","a") 

for row in range(numOfRow):
    line = ''
    for col in range(numOfCol):
        line += mapOfRooms[row][col]
    line+= '\n'
    newFile.write(line)

f.close()


