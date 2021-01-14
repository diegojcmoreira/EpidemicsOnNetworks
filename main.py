import random
from matplotlib import animation

from dataset_controller import *
from graph_utils import *
from epidemics_controller import *


if __name__ == '__main__':
    graph = load_mtx_grahp('D:\\Users\\diego\\Downloads\\socfb-Maine59\\socfb-Maine59.mtx')
    #influential_nodes_closeness = get_influential_nodes_closeness(graph)
    #influential_nodes_voterank = get_influential_nodes_voterank(graph)

    influential_nodes_voterank = [7890, 974, 75, 979, 1728, 7915, 940, 5482, 3210, 5173]
    influential_nodes_closeness = [7890, 974, 75, 7915, 1728, 940, 5482, 979, 2874, 8293]

    random_nodes = random.choices(list(graph.nodes),k=5)



    simulation_closeness = epidemy_with_recover(graph, influential_nodes_closeness[0:5], 0.05, 0.25, plot_tittle='Closeness. Inicio em 5 Vértices', return_full_data=False)
    simulation_voterank = epidemy_with_recover(graph, influential_nodes_voterank[0:5], 0.05, 0.25, plot_tittle='VoteRank. Inicio em 5 Vértices', return_full_data=False)
    simulation_aleatorio = epidemy_with_recover(graph, random_nodes[0:5], 0.05, 0.25, plot_tittle='Aleatório. Inicio em 5 Vértices',
                                                  return_full_data=False)


    # epidemy_without_recover(graph, random_nodes[0], 0.05, plot_tittle='Aleatório')
    #
    # plt.xlim(0, 700)
    # plt.ylim(0, graph.number_of_nodes())
    #
    # plt.show()
