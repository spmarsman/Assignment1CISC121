import math
#Cyclic Rotation
def rotate(rotationList, numOfRotations):
    #checking if list will work with the technique to move lists
    if length(rotationList) != 0:
        for x in range(len(rotationList)):
            #Remove last digit and put it at the begining
            tempNum = list[-1]
            list.remove[-1]
            list.insert(tempNum, 0)
    #return rotated list
    return rotationList

#FrogJmp
def jmp(X,Y,D):
    #Finding distance needed to travel
    distToGo = Y - X
    #getting the minimum amount of moves needed to move to Y from X
    numOfTimes = math.ceil(distToGo / D)
    #return number of jumps
    return numOfTimes

#permCheck
def check(permList):
    perm = True
    runningTotal = []
    #Going through every number in list
    for x in range(len(permList)):
        #Checking if the current number breaks the rules
        if permList[x] in runningTotal or permList[x] > len(permList):
            #signaling that it broke the rules
            perm = False
            break
        else:
            #Adding it to check in the future if it breaks the rules
            runningTotal.append(permList[x])
    #returning result
    if perm == True:
        return 1
    else:
        return 0

#FrogRiver
def frog(frogList, location):
    runningTotal = []
    #Going through the series of leaves in their order
    for x in range(len(frogList)):
        #checking if it is in the running total or if it is irelevant due to being before the destination
        if frogList[x-1] not in runningTotal and frogList[x-1] <= location:
            runningTotal.append(frogList[x-1])
            #if the length of the running total is equal to the destination then it is the first possible option
            if len(runningTotal) == location:
                return f"{x-1} is the earliest that the frog can cross the river"

#Passing Cars
def cars(carList):
    total = 0
    #going through cars in order
    for x in range(len(carList)):
        #Checking if to start the addition through the rest of the list
        if carList[x] == 0:
            #going through the rest of the list to see if there is a 1
            for y in range(len(carList)-x):
                if list[x + y] == 1:
                    total += 1
    #returning the total
    return f"{total} is the amount of passing cars"
