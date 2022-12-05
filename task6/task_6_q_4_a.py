from typing import List
import networkx as nx


# ----------------------------------------------
# ---------------------Q4-----------------------
# ----------------------------------------------
# the function get a graph and return if there is a cycle in the graph
# , that the value of the multiply of the cycle edges values is lower then 1
def findCycleVal(graph: nx.Graph):
    currentCycles = (nx.recursive_simple_cycles(graph))
    # go over al the possible cycles in the graph
    for currCycle in currentCycles:
        multiplyVal = 1
        i = 0
        prevNode = currCycle[i]
        i = i + 1
        # go over all the edges in the current cycle
        while i < len(currCycle):
            currNode = currCycle[i]
            # multiply the current amount with the edges value
            multiplyVal = multiplyVal * graph[prevNode][currNode]["weight"]
            prevNode = currNode
            i = i + 1
        i = currCycle[0]
        multiplyVal = multiplyVal * graph[prevNode][i]["weight"]
        if multiplyVal < 1:
            return currCycle
    return None


# the function gets a graph and a number, then adds number times of nodes to the graph
def createGraphNodes(graph: nx.Graph, nodesNum):
    H = nx.path_graph(nodesNum)
    graph.add_nodes_from(H)


# the function gets a graph and a list of edges , each edge contain 3 numbers: first: start node, second: end node ,
# third: wight of the edge. the function adds all the edges to the graph with the wight for each edge
def createGraphEdges(graph: nx.Graph, edgesNWeight: List[List[float]]):
    for currEdge in edgesNWeight:
        graph.add_edge(currEdge[0], currEdge[1], weight=currEdge[2])


if __name__ == '__main__':
    # check createGraphNodes function
    G00 = nx.DiGraph()
    createGraphNodes(G00, 10)
    assert str(G00.nodes) == '[0, 1, 2, 3, 4, 5, 6, 7, 8, 9]'

    # check createGraphEdges function
    G01 = nx.DiGraph()
    createGraphNodes(G01, 10)
    createGraphEdges(G01, [[1, 2, 10], [2, 3, 0.3], [3, 4, 0.5], [4, 5, 2], [5, 0, 6], [0, 1, 0.01]])
    assert str(G01.edges) == '[(0, 1), (1, 2), (2, 3), (3, 4), (4, 5), (5, 0)]'

    # main check for findCycleVal function and createGraphEdges,createGraphNodes
    G0 = nx.DiGraph()
    createGraphNodes(G0, 10)
    assert findCycleVal(G0) is None
    G1 = nx.DiGraph()
    createGraphNodes(G1, 4)
    createGraphEdges(G1, [[1, 2, 4], [2, 3, 2], [3, 1, 0.1]])
    assert str(findCycleVal(G1)) == '[1, 2, 3]'
    G2 = nx.DiGraph()
    createGraphNodes(G2, 4)
    createGraphEdges(G2, [[1, 2, 4], [2, 3, 2], [3, 1, 2]])
    assert findCycleVal(G2) is None
    G3 = nx.DiGraph()
    createGraphNodes(G3, 6)
    createGraphEdges(G3, [[1, 2, 10], [2, 3, 0.3], [3, 4, 0.5], [4, 5, 2], [5, 0, 6], [0, 1, 0.01]])
    assert str(findCycleVal(G3)) == '[0, 1, 2, 3, 4, 5]'
    G4 = nx.DiGraph()
    createGraphNodes(G4, 6)
    createGraphEdges(G4, [[1, 2, 10], [2, 3, 0.3], [3, 4, 1], [4, 5, 2], [5, 0, 6], [0, 1, 0.1]])
    assert findCycleVal(G4) is None
    G5 = nx.DiGraph()
    createGraphNodes(G5, 4)
    createGraphEdges(G5, [[1, 0, 0.5], [0, 1, 2], [0, 2, 0.5], [2, 3, 2], [3, 0, 0.2]])
    assert str(findCycleVal(G5)) == '[0, 2, 3]'
    G6 = nx.DiGraph()
    createGraphNodes(G6, 4)
    createGraphEdges(G6, [[1, 0, 0.5], [0, 1, 2], [0, 2, 0.5], [2, 3, 2]])
    assert findCycleVal(G6) is None
    G7 = nx.DiGraph()
    createGraphNodes(G7, 10)
    createGraphEdges(G7, [[0, 1, 0.5], [1, 0, 3], [1, 2, 0.2], [2, 0, 0.14]])
    assert str(findCycleVal(G7)) == '[0, 1, 2]'
    G8 = nx.DiGraph()
    createGraphNodes(G8, 10)
    createGraphEdges(G8, [[0, 1, 0.5], [1, 2, 3], [2, 3, 0.2], [3, 4, 0.14], [4, 5, 0.5], [5, 6, 4], [6, 7, 0.02],
                          [7, 0, 0.224], [1, 0, 1], [2, 1, 3], [3, 2, 1.2], [4, 3, 0.8], [4, 5, 0.75], [6, 5, 1.6],
                          [7, 6, 4], [0, 7, 0.02]])
    assert str(findCycleVal(G8)) == '[0, 1, 2, 3, 4, 5, 6, 7]'
    G9 = nx.DiGraph()
    createGraphNodes(G9, 10)
    createGraphEdges(G9, [[1, 2, 3], [2, 3, 0.2], [3, 4, 0.14], [4, 5, 0.5], [5, 6, 4], [6, 7, 0.02],
                          [7, 0, 0.224]])
    assert findCycleVal(G9) is None
