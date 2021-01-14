import networkx as nx
import numpy as np

from scipy.io import mmread
from matrixconverters.read_ptv import ReadPTVMatrix

import pandas as pd


def load_mtx_grahp(filename):

    mtx_file = mmread(filename)
    df_matrix = pd.DataFrame.sparse.from_spmatrix(mtx_file)

    graph = nx.from_pandas_adjacency(df_matrix)

    print("Grafo gerado com sucesso")

    return graph


def load_edgelist_graph(filename):
    graph = nx.read_edgelist(filename,comments='%')

    return graph
