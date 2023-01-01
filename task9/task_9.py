from typing import List, Dict
import networkx as nx
import matplotlib.pyplot as plt


# ----------------------------------------------
# ---------------------Q4-----------------------
# ----------------------------------------------

# the function get a total amount to share between the players,
# a list of string subjects, and a list of the preferences of the players, each player have a list of strings of his
# preferences. the function share the total amount of money between the subjects by the player preferences and use the
# Otilitery_Budget algorithm with condition
# the function returns a list of budgets by subjects
def Otilitery_Budget(total: float, subjects: List[str], preferences: List[List[str]]):
    graph = nx.Graph()
    color_map = []
    players_num = len(preferences)
    # init the graph edges and nodes
    Init_Graph(graph, subjects, players_num, color_map)
    subjects_score = {}
    subjects_full_budget = {}
    player_budget = total / players_num
    # go over al players preferences and add the right score for each preference in the subject_score dictionary
    Get_Subjects_Score(preferences, subjects_score, players_num, graph)
    # go over all the players
    for i in range(players_num):
        highest_score = 0
        highest_pref_sub = []
        # go over all the current player preferences
        for subject in preferences[i]:
            if subjects_score[subject] == highest_score:
                highest_pref_sub.append(subject)
            elif subjects_score[subject] > highest_score:
                highest_pref_sub.clear()
                highest_pref_sub.append(subject)
                highest_score = subjects_score[subject]
        subjects_budget = player_budget / (len(highest_pref_sub))
        # go over all the highest ranked preferences of the current player
        for pref_subject in highest_pref_sub:
            # set edge wight by the budget set for the current subject
            graph[i][pref_subject]['weight'] = round(subjects_budget, 2)
            if pref_subject in subjects_full_budget.keys():
                subjects_full_budget[pref_subject] += subjects_budget
            else:
                subjects_full_budget[pref_subject] = subjects_budget
            print("player " + str(i) + " gives " + str(subjects_budget) + " to " + pref_subject)
    subjects_list_budget = []
    # create a list that contain all the subcet and the budget they got by the algorithm
    Create_Budget_list(subjects, subjects_list_budget, subjects_full_budget)
    # show the connections in the graph
    Show_Graph(graph, color_map)
    return subjects_list_budget


# the function get a list of the preferences of the players, each player have a list of strings of his preferences,
# a dictionary that is first empty ,the number of players and a graph. the function calculate the amount of score to
# give for each subject by the amount it has been seen in the players preferences. store thr score in the subjects_score
def Get_Subjects_Score(preferences: List[List[str]], subjects_score: Dict[str, int], players_num: int, graph: nx.Graph):
    for i in range(players_num):
        for subject_preference in preferences[i]:
            graph.add_edge(i, subject_preference, weight=0)
            if subject_preference in subjects_score.keys():
                subjects_score[subject_preference] += 1
            else:
                subjects_score[subject_preference] = 1


# the function get  a list of string subjects,graph, the number of players and a color_map .
# the function insert to the graph the subjects as string nodes and the players a int
# the function also creates a color_map that hols the color for each node
def Init_Graph(graph: nx.Graph, subjects: List[str], number_of_players: int, color_map: List[str]):
    graph.add_nodes_from(subjects)
    players_numbers = []
    for i in range(len(subjects)):
        color_map.append('blue')
    for j in range(number_of_players):
        color_map.append('red')
        players_numbers.append(j)
    graph.add_nodes_from(players_numbers)


# the function get a graph,a color_map that contain a color for each node .
# the function draw the graph edges and nodes
def Show_Graph(graph: nx.Graph, color_map: List[str]):
    all_edges = [(u, v) for (u, v, d) in graph.edges(data=True)]
    pos = nx.random_layout(graph)  # positions for all nodes - seed for reproducibility

    # nodes
    nx.draw_networkx_nodes(graph, pos, node_color=color_map)

    # edges
    nx.draw_networkx_edges(
        graph, pos, edgelist=all_edges, width=6, alpha=0.5, edge_color="b", style="dashed"
    )

    # node labels
    nx.draw_networkx_labels(graph, pos, font_size=10, font_family="sans-serif")
    # edge weight labels
    edge_labels = nx.get_edge_attributes(graph, "weight")
    nx.draw_networkx_edge_labels(graph, pos, edge_labels, font_size=7)

    plt.show()


# the function get a list of string subjects, a dictionary that contain each subject and the budget it got by the
# algorithm - subjects_full_budget, and an empty list that will be filled with the subjects budget -
# subjects_list_budget
# the function fill the list with the values of the budget for each subject by the correct
# location of the subject
def Create_Budget_list(subjects: List[str], subjects_list_budget: List[float], subjects_full_budget: Dict[str,float]):
    print_str = "("
    for i in range(len(subjects)):
        cur_score = 0
        if subjects[i] in subjects_full_budget.keys():
            cur_score = subjects_full_budget[subjects[i]]
        subjects_list_budget.append(cur_score)
        print_str = print_str + subjects[i] + " : " + str(cur_score) + ", "
    print_str = print_str + ")"
    print(print_str)
    print(" ")


if __name__ == '__main__':
    # check Get_Subjects_Score function
    graph0 = nx.Graph()
    subjects_score00 = {}
    preferences00 = [["food", "sport"], ["sleep"]]
    player_num0 = len(preferences00)
    Get_Subjects_Score(preferences00, subjects_score00, player_num0, graph0)
    assert str(subjects_score00) == "{'food': 1, 'sport': 1, 'sleep': 1}"

    graph1 = nx.Graph()
    subjects_score01 = {}
    preferences01 = [["pool", "gym"], ["sauna", "showers"], ["sauna", "gym"]]
    player_num1 = len(preferences01)
    Get_Subjects_Score(preferences01, subjects_score01, player_num1, graph1)
    assert str(subjects_score01) == "{'pool': 1, 'gym': 2, 'sauna': 2, 'showers': 1}"

    graph2 = nx.Graph()
    subjects_score02 = {}
    preferences02 = [["school", "mall", "roads"], ["mall", "roads", "parks"], ["roads", "parks", "events"],
                     ["parks", "events", "school"], ["mall", "events", "school"]]
    player_num2 = len(preferences02)
    Get_Subjects_Score(preferences02, subjects_score02, player_num2, graph2)
    assert str(subjects_score02) == "{'school': 3, 'mall': 3, 'roads': 3, 'parks': 3, 'events': 3}"

    # check Create_Budget_list function
    subjects_list_budget10 = []
    subjects10 = ["food", "sport", "sleep"]
    subjects_full_budget10 = {'food': 250.0, 'sport': 250.0, 'sleep': 500.0}
    Create_Budget_list(subjects10,subjects_list_budget10,subjects_full_budget10)
    assert str(subjects_list_budget10) == "[250.0, 250.0, 500.0]"

    subjects_list_budget11 = []
    subjects11 = ["pool", "gym", "jacuzzi", "sauna", "spa", "showers"]
    subjects_full_budget11 = {'gym': 400.0, 'sauna': 400.0}
    Create_Budget_list(subjects11,subjects_list_budget11,subjects_full_budget11)
    assert str(subjects_list_budget11) == "[0, 400.0, 0, 400.0, 0, 0]"

    subjects_list_budget12 = []
    subjects12 = ["school", "mall", "roads", "parks", "events"]
    subjects_full_budget12 = {'school': 510.4, 'mall': 510.4, 'roads': 510.4, 'parks': 510.4, 'events': 510.4}
    Create_Budget_list(subjects12,subjects_list_budget12,subjects_full_budget12)
    assert str(subjects_list_budget12) == "[510.4, 510.4, 510.4, 510.4, 510.4]"

    # check Otilitery_Budget function
    total0 = 1000
    subjects0 = ["food", "sport", "sleep"]
    preferences0 = [["food", "sport"], ["sleep"]]
    assert str(Otilitery_Budget(total0, subjects0, preferences0)) == '[250.0, 250.0, 500.0]'

    total1 = 800
    subjects1 = ["pool", "gym", "jacuzzi", "sauna", "spa", "showers"]
    preferences1 = [["pool", "gym"], ["sauna", "showers"], ["sauna", "gym"]]
    assert str(Otilitery_Budget(total1, subjects1, preferences1)) == '[0, 400.0, 0, 400.0, 0, 0]'

    total2 = 2552
    subjects2 = ["school", "mall", "roads", "parks", "events"]
    preferences2 = [["school", "mall", "roads"], ["mall", "roads", "parks"], ["roads", "parks", "events"],
                    ["parks", "events", "school"], ["mall", "events", "school"]]
    assert str(Otilitery_Budget(total2, subjects2, preferences2)) == '[510.4, 510.4, 510.4, 510.4, 510.4]'

    total3 = 10
    subjects3 = ["floor1", "floor2", "floor3"]
    preferences3 = [["floor1"], ["floor2"], ["floor3"],
                    ["floor3", "floor1"]]
    assert str(Otilitery_Budget(total3, subjects3, preferences3)) == '[3.75, 2.5, 3.75]'

    total4 = 50
    subjects4 = ["mcdonald", "KFC", "burger king", "domino's", "starbucks"]
    preferences4 = [["KFC", "mcdonald"], ["mcdonald", "burger king"], ["mcdonald"],
                    ["KFC"]]
    assert str(Otilitery_Budget(total4, subjects4, preferences4)) == '[37.5, 12.5, 0, 0, 0]'
