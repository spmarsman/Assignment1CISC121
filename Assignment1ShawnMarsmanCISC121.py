import math
#Cyclic Rotation
def rotate(rotationList, numOfRotations):
    if length(rotationList) != 0:
        for x in range(len(rotationList)):
            tempNum = list[-1]
            list.remove[-1]
            list.insert(tempNum, 0)
    return rotationList

#FrogJmp
def jmp(X,Y,D):
    distToGo = Y - X
    numOfTimes = math.ceil(distToGo / D)
    return numOfTimes

#permCheck
def check(permList):
    perm = True
    runningTotal = []
    for x in range(len(permList)):
        if permList[x] in runningTotal or permList[x] > len(permList):
            perm = False
            break
        else:
            runningTotal.append(permList[x])
    if perm == True:
        return 1
    else:
        return 0

#FrogRiver
def frog(frogList, location):
    runningTotal = []
    for x in range(len(frogList)):
        if frogList[x-1] not in runningTotal and frogList[x-1] <= location:
            runningTotal.append(frogList[x-1])
            if len(runningTotal) == location:
                return f"{x-1} is the earliest that the frog can cross the river"

#Passing Cars
def cars(carList):
    total = 0
    for x in range(len(carList)):
        if carList[x] == 0:
            for y in range(len(carList)-x):
                if list[x + y] == 1:
                    total += 1
    return f"{total} is the amount of passing cars"
