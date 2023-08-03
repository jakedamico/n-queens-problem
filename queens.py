import numpy as np
import re
import sys
import random
np.set_printoptions(threshold=sys.maxsize)
#changes the print settings to allow the entire array to be displayed

#struggled with initializing the numpy arrays properly
currentStateConflicts = 0
currentState = np.array([

    [0, 0, 0, 0, 0, 0, 0, 0],
    [0, 0, 0, 0, 0, 0, 0, 0],
    [0, 0, 0, 0, 0, 0, 0, 0],
    [0, 0, 0, 0, 0, 0, 0, 0],
    [0, 0, 0, 0, 0, 0, 0, 0],
    [0, 0, 0, 0, 0, 0, 0, 0],
    [0, 0, 0, 0, 0, 0, 0, 0],
    [0, 0, 0, 0, 0, 0, 0, 0],

])

#added two zeros to correspond to the two empty boards in the neighboring states
neighboringStateConflicts = [0, 0]
totalNeighboringStates = 0
neighboringStates = np.array([

    [[0, 0, 0, 0, 0, 0, 0, 0],
     [0, 0, 0, 0, 0, 0, 0, 0],
     [0, 0, 0, 0, 0, 0, 0, 0],
     [0, 0, 0, 0, 0, 0, 0, 0],
     [0, 0, 0, 0, 0, 0, 0, 0],
     [0, 0, 0, 0, 0, 0, 0, 0],
     [0, 0, 0, 0, 0, 0, 0, 0],
     [0, 0, 0, 0, 0, 0, 0, 0]],

    [[0, 0, 0, 0, 0, 0, 0, 0],
     [0, 0, 0, 0, 0, 0, 0, 0],
     [0, 0, 0, 0, 0, 0, 0, 0],
     [0, 0, 0, 0, 0, 0, 0, 0],
     [0, 0, 0, 0, 0, 0, 0, 0],
     [0, 0, 0, 0, 0, 0, 0, 0],
     [0, 0, 0, 0, 0, 0, 0, 0],
     [0, 0, 0, 0, 0, 0, 0, 0]]

])

numOfQueens = input('Enter the number of queens to be placed:')
queensReach = input('Enter the distance the queens can attack:')
queensLocations = input('Enter the locations of the queens:')


def splitQueensInput(queensCoordinates):
    return re.sub('\D', '', queensCoordinates)


def inputIntoState(queensLocations):
    for x in range(0, int(numOfQueens), 1):
        start = x * 2
        queensLocationsNumbers = splitQueensInput(queensLocations)
        x = int(queensLocationsNumbers[start]) - 1
        y = int(queensLocationsNumbers[start + 1]) - 1
        currentState[x][y] = 1


def locateQueen(board, queenNum):
    queenCounter = 0
    for i in range(len(board)):
        for j in range(len(board[i])):
            if board[i][j] == 1:
                queenCounter = queenCounter + 1
                if queenCounter == queenNum:
                    return (int(str(i + 1) + str(j + 1)))


def locateAllQueens(board):
    for i in range(len(board)):
        for j in range(len(board[i])):
            if board[i][j] == 1:
                return int(str(i + 1) + str(j + 1))


def findConflicts(searchType, stateToSearch, stateType, neighborNum=None):
    if stateType == 'current':
        global currentStateConflicts
    else:
        global neighboringStateConflicts

    # Top left diagonal
    if searchType == 'TL':
        for x in range(1, int(numOfQueens)+1, 1):
            queenLocation = str(locateQueen(stateToSearch, x))
            x = int(queenLocation[0])
            y = int(queenLocation[1])
            for i in range(0, int(queensReach), 1):
                x = x - 1
                y = y - 1
                try:
                    stateToSearch[x-1][y-1]
                except IndexError:
                    break
                except TypeError:
                    break
                if y-1 == -1 or x-1 == -1:
                    break
                if stateToSearch[x-1][y-1] == 1:
                    if stateType == 'current':
                        currentStateConflicts = currentStateConflicts + 1
                    else:
                        neighboringStateConflicts[neighborNum] = neighboringStateConflicts[neighborNum] + 1

    # Top right diagonal
    elif searchType == 'TR':
        for x in range(1, int(numOfQueens)+1, 1):
            queenLocation = str(locateQueen(stateToSearch, x))
            x = int(queenLocation[0])
            y = int(queenLocation[1])
            for i in range(0, int(queensReach), 1):
                x = x - 1
                y = y + 1
                try:
                    stateToSearch[x-1][y-1]
                except IndexError:
                    break
                except TypeError:
                    break
                if y-1 == -1 or x-1 == -1:
                    break
                if stateToSearch[x - 1][y - 1] == 1:
                    if stateType == 'current':
                        currentStateConflicts = currentStateConflicts + 1
                    else:
                        neighboringStateConflicts[neighborNum] = neighboringStateConflicts[neighborNum] + 1

    # Bottom left diagonal
    elif searchType == 'BL':
        for x in range(1, int(numOfQueens)+1, 1):
            queenLocation = str(locateQueen(stateToSearch, x))
            x = int(queenLocation[0])
            y = int(queenLocation[1])
            for i in range(0, int(queensReach), 1):
                x = x + 1
                y = y - 1
                try:
                    stateToSearch[x - 1][y - 1]
                except IndexError:
                    break
                except TypeError:
                    break
                if y-1 == -1 or x-1 == -1:
                    break
                if stateToSearch[x - 1][y - 1] == 1:
                    if stateType == 'current':
                        currentStateConflicts = currentStateConflicts + 1
                    else:
                        neighboringStateConflicts[neighborNum] = neighboringStateConflicts[neighborNum] + 1

    # Bottom right diagonal
    elif searchType == 'BR':
        for x in range(1, int(numOfQueens)+1, 1):
            queenLocation = str(locateQueen(stateToSearch, x))
            x = int(queenLocation[0])
            y = int(queenLocation[1])
            for i in range(0, int(queensReach), 1):
                x = x + 1
                y = y + 1
                try:
                    stateToSearch[x-1][y-1]
                except IndexError:
                    break
                except TypeError:
                    break
                if y-1 == -1 or x-1 == -1:
                    break
                if stateToSearch[x - 1][y - 1] == 1:
                    if stateType == 'current':
                        currentStateConflicts = currentStateConflicts + 1
                    else:
                        neighboringStateConflicts[neighborNum] = neighboringStateConflicts[neighborNum] + 1

    # Left
    elif searchType == 'L':
        for x in range(1, int(numOfQueens)+1, 1):
            queenLocation = str(locateQueen(stateToSearch, x))
            x = int(queenLocation[0])
            y = int(queenLocation[1])
            for i in range(0, int(queensReach), 1):
                y = y - 1
                try:
                    stateToSearch[x-1][y-1]
                except IndexError:
                    break
                except TypeError:
                    break
                if y-1 == -1 or x-1 == -1:
                    break
                if stateToSearch[x - 1][y - 1] == 1:
                    if stateType == 'current':
                        currentStateConflicts = currentStateConflicts + 1
                    else:
                        neighboringStateConflicts[neighborNum] = neighboringStateConflicts[neighborNum] + 1

    # Right
    elif searchType == 'R':
        for x in range(1, int(numOfQueens)+1, 1):
            queenLocation = str(locateQueen(stateToSearch, x))
            x = int(queenLocation[0])
            y = int(queenLocation[1])
            for i in range(0, int(queensReach), 1):
                y = y + 1
                try:
                    stateToSearch[x-1][y-1]
                except IndexError:
                    break
                except TypeError:
                    break
                if y-1 == -1 or x-1 == -1:
                    break
                if stateToSearch[x - 1][y - 1] == 1:
                    if stateType == 'current':
                        currentStateConflicts = currentStateConflicts + 1
                    else:
                        neighboringStateConflicts[neighborNum] = neighboringStateConflicts[neighborNum] + 1

    # Above
    elif searchType == 'A':
        for x in range(1, int(numOfQueens)+1, 1):
            queenLocation = str(locateQueen(stateToSearch, x))
            x = int(queenLocation[0])
            y = int(queenLocation[1])
            for i in range(0, int(queensReach), 1):
                x = x - 1
                try:
                    stateToSearch[x-1][y-1]
                except IndexError:
                    break
                except TypeError:
                    break
                if y-1 == -1 or x-1 == -1:
                    break
                if stateToSearch[x - 1][y - 1] == 1:
                    if stateType == 'current':
                        currentStateConflicts = currentStateConflicts + 1
                    else:
                        neighboringStateConflicts[neighborNum] = neighboringStateConflicts[neighborNum] + 1

    # Below
    elif searchType == 'B':
        for x in range(1, int(numOfQueens)+1, 1):
            queenLocation = str(locateQueen(stateToSearch, x))
            x = int(queenLocation[0])
            y = int(queenLocation[1])
            for i in range(0, int(queensReach), 1):
                x = x + 1
                try:
                    stateToSearch[x-1][y-1]
                except IndexError:
                    break
                except TypeError:
                    break
                if y-1 == -1 or x-1 == -1:
                    break
                if stateToSearch[x - 1][y - 1] == 1:
                    if stateType == 'current':
                        currentStateConflicts = currentStateConflicts + 1
                    else:
                        neighboringStateConflicts[neighborNum] = neighboringStateConflicts[neighborNum] + 1
    return


def findAllCurrentConflicts():
    findConflicts('TL', currentState, 'current')
    findConflicts('TR', currentState, 'current')
    findConflicts('BL', currentState, 'current')
    findConflicts('BR', currentState, 'current')
    findConflicts('L', currentState, 'current')
    findConflicts('R', currentState, 'current')
    findConflicts('A', currentState, 'current')
    findConflicts('B', currentState, 'current')
    return


def findAllNeighborConflicts():
    for x in range(len(neighboringStates)):
        findConflicts('TL', neighboringStates[x], 'neighbor', x)
        findConflicts('TR', neighboringStates[x], 'neighbor', x)
        findConflicts('BL', neighboringStates[x], 'neighbor', x)
        findConflicts('BR', neighboringStates[x], 'neighbor', x)
        findConflicts('L', neighboringStates[x], 'neighbor', x)
        findConflicts('R', neighboringStates[x], 'neighbor', x)
        findConflicts('A', neighboringStates[x], 'neighbor', x)
        findConflicts('B', neighboringStates[x], 'neighbor', x)
    return


def addToNeighboringStates(stateToAdd):
    global neighboringStates
    neighboringStates = np.concatenate((neighboringStates, np.array([stateToAdd])))
    return


def removeBlanksFromNeighboring():
    global neighboringStates
    neighboringStates = np.delete(neighboringStates, 0, 0)
    neighboringStates = np.delete(neighboringStates, 0, 0)
    neighboringStateConflicts.pop()
    neighboringStateConflicts.pop()
    return


def createNeighboringStates():
    for x in range(1, int(numOfQueens) + 1, 1):
        queenLocation = locateQueen(currentState, x)
        for i in range(8):
            for j in range(8):
                if int(str(i + 1) + str(j + 1)) == queenLocation:
                    continue

                newNeighboringState = np.copy(currentState)
                newNeighboringState[int(str(queenLocation)[0])-1][int(str(queenLocation)[1])-1] = 0
                if newNeighboringState[i][j] == 1:
                    continue
                newNeighboringState[i][j] = 1
                addToNeighboringStates(newNeighboringState)

                neighboringStateConflicts.append(0)
    return


def pickNextState():
    global currentStateConflicts
    global neighboringStateConflicts
    global neighboringStates
    global totalNeighboringStates
    lowestConflictsList = min(neighboringStateConflicts)
    lowestConflictIndex = random.choice([i for i in range(len(neighboringStateConflicts)) if neighboringStateConflicts[i] == lowestConflictsList])
    if currentStateConflicts >= neighboringStateConflicts[lowestConflictIndex]:
        global currentState
        currentState = np.copy(neighboringStates[lowestConflictIndex])
        currentStateConflicts = int(neighboringStateConflicts[lowestConflictIndex])

    totalNeighboringStates = totalNeighboringStates + int(len(neighboringStates))
    neighboringStateConflicts = [0, 0]
    neighboringStates = np.array([

        [[0, 0, 0, 0, 0, 0, 0, 0],
         [0, 0, 0, 0, 0, 0, 0, 0],
         [0, 0, 0, 0, 0, 0, 0, 0],
         [0, 0, 0, 0, 0, 0, 0, 0],
         [0, 0, 0, 0, 0, 0, 0, 0],
         [0, 0, 0, 0, 0, 0, 0, 0],
         [0, 0, 0, 0, 0, 0, 0, 0],
         [0, 0, 0, 0, 0, 0, 0, 0]],

        [[0, 0, 0, 0, 0, 0, 0, 0],
         [0, 0, 0, 0, 0, 0, 0, 0],
         [0, 0, 0, 0, 0, 0, 0, 0],
         [0, 0, 0, 0, 0, 0, 0, 0],
         [0, 0, 0, 0, 0, 0, 0, 0],
         [0, 0, 0, 0, 0, 0, 0, 0],
         [0, 0, 0, 0, 0, 0, 0, 0],
         [0, 0, 0, 0, 0, 0, 0, 0]]

    ])
    return


def main():

    inputIntoState(splitQueensInput(queensLocations))
    findAllCurrentConflicts()
    print('Starting State:')
    print(currentState)
    print('Current # of conflicts: ' + str(currentStateConflicts))
    print('-----------------------------')

    i = 0
    while True:

        createNeighboringStates()
        removeBlanksFromNeighboring()
        findAllNeighborConflicts()

        pickNextState()
        i = i + 1
        if i <= 4:
            print('Board after ' + str(i) + ' iterations:')
            print(currentState)
            print('Conflicts after ' + str(i) + ' iterations: ' + str(currentStateConflicts))
            print('-----------------------------')

        if currentStateConflicts == 0:
            print('SOLUTION FOUND')
            print(currentState)
            print('Final state number of conflicts: ' + str(currentStateConflicts))
            print('Total iterations: ' + str(i))
            print('Total neighboring states examined: ' + str(totalNeighboringStates))
            break

        if i > 60:
            print('MAX ITERATIONS REACHED (60)')
            print(currentState)
            print('Final state number of conflicts: ' + str(currentStateConflicts))
            print('Total iterations: ' + str(i))
            print('Total neighboring states examined: ' + str(totalNeighboringStates))
            break

    return


main()