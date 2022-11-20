from typing import List
import copy


# ----------------------------------------------
# -----------------State-class------------------
# ----------------------------------------------
# class of the a state, contains the current value for each player and the number of items that have been distribute
class State:
    def __init__(self, allValues: List[int], item: int):
        self.allValues = []
        for i in range(len(allValues)):
            self.allValues.append(allValues[i])
        self.item = item

    # update the current value of the player by the location
    def updateVal(self, location: int, val: int):
        self.allValues[location] += val

    # update the amount of items that have been distributed in this state
    def updateItem(self, item: int):
        self.item = item

    # check if the states are equal by the players current values and by the  amount of items that have been
    # distributed in this state
    def __eq__(self, other):
        if isinstance(other, State) is False:
            return False
        if self.item != other.item:
            return False
        for i in range(len(self.allValues)):
            if self.allValues[i] != other.allValues[i]:
                return False
        return True


# return the minimum value in the state
def minInState(currState: State):
    minVal = currState.allValues[0]
    for i in range(1, len(currState.allValues)):
        if currState.allValues[i] < minVal:
            minVal = currState.allValues[i]
    return minVal


# return the state with the maximum of the minimum value
def maxOfMin(finalStates: List[State]):
    minVal = minInState(finalStates[0])
    currState = finalStates[0]
    for i in range(1, len(finalStates)):
        currVal = minInState(finalStates[i])
        if currVal > minVal:
            minVal = currVal
            currState = finalStates[i]
    return currState


# ----------------------------------------------
# ---------------------Q1-----------------------
# ----------------------------------------------
# search in the state space, and return all the available final states and the state with the max minimum
def findAllStates(playersValues, playersAmount: int, itemsAmount: int):
    allStates = []
    finalStates = []
    firstStateValues = []
    # initiate the values of the players
    for i in range(playersAmount):
        firstStateValues.append(0)
    firstState = State(firstStateValues, 0)
    allStates.append(firstState)
    findAllStatesInner(finalStates, allStates, playersValues, playersAmount, 0, itemsAmount, firstState)
    return [finalStates, maxOfMin(finalStates)]


# search in the current state space, and update the state list with the current possible state
def findAllStatesInner(finalStates: List[State], allStates: List[State], playersValues, playersAmount: int,
                       itemsDistribute: int,
                       itemsAmount: int, prevState: State):
    # check the number of items that have been distributed
    if itemsDistribute >= itemsAmount:
        return
    # go over all the possible states from the prev state, update the current state by the item value for the player
    #  and update the item by the amount of items that have been distributed in this state
    for i in range(playersAmount):
        currState = copy.deepcopy(prevState)
        currState.updateVal(i, playersValues[itemsDistribute][i])
        currState.updateItem(itemsDistribute + 1)
        allStates.append(currState)
        if itemsDistribute + 1 == itemsAmount:
            finalStates.append(currState)
        findAllStatesInner(finalStates, allStates, playersValues, playersAmount, itemsDistribute + 1, itemsAmount,
                           currState)


# ----------------------------------------------
# ---------------------Q2-----------------------
# ----------------------------------------------
# check if a current state is in the state list
def findState(allStates: List[State], currState: State):
    for i in range(len(allStates)):
        if allStates[i] == currState:
            return True
    return False


# search in the state space, and return all the available final states and the state with the max minimum
# this function use chopping , a state that has already been in the state list will not be inserted again
def findAllStatesWithChop(playersValues, playersAmount: int, itemsAmount: int):
    allStates = []
    finalStates = []
    firstStateValues = []
    # initiate the values of the players
    for i in range(playersAmount):
        firstStateValues.append(0)
    firstState = State(firstStateValues, 0)
    allStates.append(firstState)
    findAllStatesWithChopInner(finalStates, allStates, playersValues, playersAmount, 0, itemsAmount, firstState)
    return [finalStates, maxOfMin(finalStates)]


# search in the current state space, and update the state list with the current possible state
# but after chopping ,witch mean that  a state that has already been in the state list will not be inserted again
def findAllStatesWithChopInner(finalStates: List[State], allStates: List[State], playersValues, playersAmount: int,
                               itemsDistribute: int,
                               itemsAmount: int, prevState: State):
    # check the number of items that have been distributed
    if itemsDistribute >= itemsAmount:
        return
    # go over all the possible states from the prev state, update the current state by the item value for the player
    #  and update the item by the amount of items that have been distributed in this state
    for i in range(playersAmount):
        currState = copy.deepcopy(prevState)
        currState.updateVal(i, playersValues[itemsDistribute][i])
        currState.updateItem(itemsDistribute + 1)
        #  only if the state is not in the state list , insert it
        if findState(allStates, currState) is False:
            allStates.append(currState)
            if itemsDistribute + 1 == itemsAmount:
                finalStates.append(currState)
            findAllStatesWithChopInner(finalStates, allStates, playersValues, playersAmount, itemsDistribute + 1,
                                       itemsAmount,
                                       currState)


if __name__ == '__main__':
    # check findAllStates
    Arr = [[11, 22, 33], [11, 22, 44]]
    assert len(findAllStates(Arr, 3, 2)[0]) is 9
    Arr = [[1, 2, 3, 4], [11, 22, 33, 44]]
    assert len(findAllStates(Arr, 4, 2)[0]) is 16
    Arr = [[1, 1], [11, 11], [13, 13]]
    assert len(findAllStates(Arr, 2, 3)[0]) is 8
    bestState = findAllStates(Arr, 2, 3)[1]
    currState = State([12, 13], 3)
    assert bestState == currState
    Arr = [[2, 2], [2, 2]]
    assert len(findAllStates(Arr, 2, 2)[0]) is 4
    Arr = [[11, 22, 33], [11, 22, 44], [55, 33, 0]]
    assert len(findAllStates(Arr, 3, 3)[0]) is 27
    Arr = [[1, 1], [2, 2], [1, 1]]
    assert len(findAllStates(Arr, 2, 3)[0]) is 8
    Arr = [[1, 1], [2, 2], [3, 3], [1, 1], [2, 2]]
    assert len(findAllStates(Arr, 2, 5)[0]) is 32

    # check findAllStatesWithChop
    Arr = [[2, 2], [2, 2]]
    assert len(findAllStatesWithChop(Arr, 2, 2)[0]) is 3
    Arr = [[11, 22, 33], [11, 22, 44], [55, 33, 0]]
    assert len(findAllStatesWithChop(Arr, 3, 3)[0]) is 24
    Arr = [[1, 1], [2, 2], [1, 1]]
    assert len(findAllStatesWithChop(Arr, 2, 3)[0]) is 5
    Arr = [[1, 1], [2, 2], [3, 3], [1, 1], [2, 2]]
    assert len(findAllStatesWithChop(Arr, 2, 5)[0]) is 10
