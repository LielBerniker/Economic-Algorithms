from typing import List


# ----------------------------------------------
# ---------------------Q1-----------------------
# ----------------------------------------------
# find if there is a circle in the mat
def hasCircle(playersDivision: List[List[float]]):
    visitedPlayers = {}
    # go over all the components
    for i in range(len(playersDivision)):
        #  check if the players has been visited
        if i not in visitedPlayers:
            for j in range(len(playersDivision[0])):
                if 1 > playersDivision[i][j] > 0:
                    visitedPlayers[i] = j
                    # check if there is a circle in this player component
                    circle = findCircle(playersDivision, visitedPlayers, i, j)
                    if circle is True:
                        return True
    return False


# return true or false if there is a circle in this player component
def findCircle(playersDivision: List[List[float]], visitedPlayers, currentPlayer: int, currentItem: int):
    # find all players that share this recurse
    allSharePlayers = findSharePlayers(playersDivision, currentPlayer, currentItem)
    for currPlayer in allSharePlayers:
        if currPlayer in visitedPlayers:
            return True
        visitedPlayers[currPlayer] = currentItem
        # go over all the current player recourses
        for i in range(len(playersDivision[0])):
            if i != currentItem and 1 > playersDivision[currPlayer][i] > 0:
                circle = findCircle(playersDivision, visitedPlayers, currPlayer, i)
                if circle is True:
                    return True
    return False


# find all players locations that share the specific recurse with the current player
def findSharePlayers(PlayersDivision: List[List[float]], currentPlayer: int, currentItem: int):
    sharePlayers = []
    for i in range(len(PlayersDivision)):
        if i != currentPlayer and 1 > PlayersDivision[i][currentItem] > 0:
            sharePlayers.append(i)
    return sharePlayers


if __name__ == '__main__':
    # test for circle in different mat
    Arr = [[1, 0.03, 0], [0, 0.97, 1]]
    assert hasCircle(Arr) is False
    Arr = [[1, 0.03, 0], [0, 0.94, 0.5], [0, 0.03, 0.5]]
    assert hasCircle(Arr) is True
    Arr = [[1, 0.03, 0.3], [0, 0.97, 0.7]]
    assert hasCircle(Arr) is True
    Arr = [[0.6, 0.03, 0], [0, 0.97, 1], [0.4, 0, 0]]
    assert hasCircle(Arr) is False
    Arr = [[0.6, 0, 0], [0.2, 0, 0], [0.2, 0, 0]]
    assert hasCircle(Arr) is False
    Arr = [[1, 0.5, 0, 0], [0, 0.5, 0.4, 0], [0, 0, 0.6, 0.2], [0, 0, 0, 0.8]]
    assert hasCircle(Arr) is False
    Arr = [[0.23, 0.5, 0, 0], [0, 0.5, 0.4, 0], [0, 0, 0.6, 0.2], [0.77, 0, 0, 0.8]]
    assert hasCircle(Arr) is True
    Arr = [[0.2, 0, 0], [0.7, 0, 0], [0.1, 0.1, 0.1], [0, 0, 0.6], [0, 0, 0.3]]
    assert hasCircle(Arr) is False
