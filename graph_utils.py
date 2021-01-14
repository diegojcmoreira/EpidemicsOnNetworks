import networkx as nx
import EoN

def get_influential_nodes_closeness(graph):
    print("Calculando a influencia dos vertices")
    nodes_dict = nx.closeness_centrality(graph)

    most_influential_nodes = []

    for key, value in sorted(nodes_dict.items(), key=lambda item: item[1], reverse=True):
        most_influential_nodes.append(key)

    return most_influential_nodes[0:10]


def get_influential_nodes_voterank(graph):
    print("Calculando a influencia dos vertices")
    most_influential_nodes = nx.voterank(graph)

    return most_influential_nodes[0:10]




