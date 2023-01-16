from typing import List, Dict
import doctest


# ----------------------------------------------
# --------------------Q1_A----------------------
# ----------------------------------------------

def find_trading_cycle(preferences: List[List[int]]):
    """
        the function get a list of list that contain the preferences of the
        house owners (for example). Each list in the inner list contain a list of indexes of the houses that the current
        house owner prefer.
        the function find a cycle in the preferences by the first preference of each house owner the
        function returns a list that contains the cycle, by the number of house owners followed by the house they will have
        next in the cycle
        Programmer: Liel Berniker
        >>> find_trading_cycle([[1, 2], [0, 2], [1, 0]])
        [0, 1]
        >>> find_trading_cycle([[4, 2,3,1],[4, 3,2,0],[4, 0,3,1],[4, 2,0,1],[0, 2,3,1]])
        [0, 4]
        >>> find_trading_cycle([[1, 2,3],[3, 0,2],[0, 1,3],[2, 1,0]])
        [0, 1, 3, 2]
        >>> find_trading_cycle([[1, 2,3],[0, 3,2],[3, 1,0],[2, 1,0]])
        [0, 1]
    """
    visited_nodes = {}
    preference_cycle = []
    nodes_size = len(preferences)
    # go over all the house owners
    for node in range(nodes_size):
        # check if didn't get a house yet
        if len(preferences[node]) == 0:
            continue
        best_preference = preferences[node][0]
        visited_nodes[node] = best_preference
        no_val_cycle = False
        # go over the preferences until find a cycle
        while best_preference not in visited_nodes:
            # check if the specific householder did get a match already
            if len(preferences[best_preference]) == 0:
                visited_nodes.clear()
                no_val_cycle = True
                break
            cur_preference = preferences[best_preference][0]
            visited_nodes[best_preference] = cur_preference
            best_preference = cur_preference
        if no_val_cycle:
            continue
        first_in_cycle = best_preference
        preference_cycle.append(first_in_cycle)
        cur_node = preferences[first_in_cycle][0]
        # create the list that contain the cycle
        while cur_node != first_in_cycle:
            preference_cycle.append(cur_node)
            cur_node = preferences[cur_node][0]
        break
    return preference_cycle


# ----------------------------------------------
# --------------------Q1_B----------------------
# ----------------------------------------------
def trading_cycle_algorithm(preferences: List[List[int]]):
    """
        the function get a list of list that contain the preferences of the
        house owners (for example) Each list in the inner list contain a list of indexes of the houses that the current
        house owner prefer
        the function return a dict that contain all the house numbers in the keys and their value
        is the house they got from the algorithm.
        the algorithm that been used in the function is trading cycle algorithm
        Programmer: Liel Berniker
        >>> trading_cycle_algorithm([[1, 2], [0, 2], [1, 0]])
        {0: 1, 1: 0, 2: 2}
        >>> trading_cycle_algorithm([[4, 2,3,1],[4, 3,2,0],[4, 0,3,1],[4, 2,0,1],[0, 2,3,1]])
        {0: 4, 4: 0, 1: 1, 2: 2, 3: 3}
        >>> trading_cycle_algorithm([[1, 2,3],[3, 0,2],[0, 1,3],[2, 1,0]])
        {0: 1, 1: 3, 3: 2, 2: 0}
        >>> trading_cycle_algorithm([[1, 2,3],[0, 3,2],[3, 1,0],[2, 1,0]])
        {0: 1, 1: 0, 2: 3, 3: 2}
    """
    node_match = {}
    round_num = len(preferences)
    cur_pref = 0
    # go over the householders preferences until go over all preferences list
    while cur_pref < (round_num - 1):
        cycle_in_graph = find_trading_cycle(preferences)
        cycle_len = len(cycle_in_graph)
        # if there is no cycle go to next preference of each householder that do not have a match
        if cycle_len == 0:
            for i in range(round_num):
                if len(preferences[i]) != 0:
                    preferences[i].pop(0)
            cur_pref = cur_pref + 1
        else:
            cycle_node = 0
            # add the householders that in the cycle to the dictionary
            while cycle_node < (cycle_len - 1):
                node_num = cycle_in_graph[cycle_node]
                node_match[node_num] = cycle_in_graph[cycle_node + 1]
                cycle_node = cycle_node + 1
                preferences[node_num].clear()
            node_num = cycle_in_graph[cycle_node]
            node_match[node_num] = cycle_in_graph[0]
            preferences[node_num].clear()
    # the householders that did not have a match get their own house
    for i in range(round_num):
        if i not in node_match:
            node_match[i] = i
    return node_match


if __name__ == '__main__':

    (failures, tests) = doctest.testmod(report=True, optionflags=doctest.NORMALIZE_WHITESPACE + doctest.ELLIPSIS)
    print("{} failures, {} tests".format(failures, tests))
