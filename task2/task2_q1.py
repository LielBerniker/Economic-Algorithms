# This is a sample Python script.

# Press Shift+F10 to execute it or replace it with your code.
# Press Double Shift to search everywhere for classes, files, tool windows, actions, and settings.
import re
from typing import List


class Agent:
    # Create an Agent by a list of values
    def __init__(self, allOptions: List[float]):
        self.allValues = allOptions

    # Return the value by the option, if the option is invalid return None
    # Values should be between 1 and the amount of values
    def value(self, option: int) -> float:
        option = option - 1
        if len(self.allValues) > option >= 0:
            return self.allValues[option]
        return None


# return true if option 1 is pareto improvement of option 2
# else return false
def isParetoImprovement(agents: List[Agent], option1: int,
                        option2: int) -> bool:
    better = False
    for agent in agents:
        if agent.value(option2) > agent.value(option1):
            return False
        # if one of the values is bigger better is true
        elif agent.value(option2) < agent.value(option1):
            better = True
    # check if one of hte values got a greater value
    if better is True:
        return True
    return False


# check if the current option is a pareto optimal
def isParetoOptimal(agents: List[Agent], option: int,
                    allOptions: List[int]) -> bool:
    for currOption in allOptions:
        if isParetoImprovement(agents, currOption, option) is True:
            return False
    return True


if __name__ == '__main__':
    Ami = Agent([1, 2, 3, 4, 5])
    Tami = Agent([3, 1, 2, 5, 4])
    Rami = Agent([3, 5, 5, 1, 1])
    allAgents = [Ami, Tami, Rami]
    currOptions = [1, 2, 3, 4, 5]
    # check isParetoImprovement
    answer = isParetoImprovement(allAgents, 1, 1)
    assert answer is False
    answer = isParetoImprovement(allAgents, 3, 1)
    assert answer is False
    answer = isParetoImprovement(allAgents, 3, 2)
    assert answer is True
    answer = isParetoImprovement(allAgents, 4, 5)
    assert answer is False
    answer = isParetoImprovement(allAgents, 5, 4)
    assert answer is False
    answer = isParetoImprovement(allAgents, 3, 5)
    assert answer is False
    # check isParetoOptimal
    answer = isParetoOptimal(allAgents, 1, currOptions)
    assert answer is True
    answer = isParetoOptimal(allAgents, 2, currOptions)
    assert answer is False
    answer = isParetoOptimal(allAgents, 3, currOptions)
    assert answer is True
    answer = isParetoOptimal(allAgents, 4, currOptions)
    assert answer is True
    answer = isParetoOptimal(allAgents, 5, currOptions)
    assert answer is True
