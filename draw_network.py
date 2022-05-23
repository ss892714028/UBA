from config import trans_matrix, nodes


import matplotlib.pyplot as plt
import networkx as nx
import pandas as pd

options = {
    'node_color': 'blue',
    'node_size': 30,
    'width': 1,
    'arrowstyle': '-|>',
    'arrowsize': 4,
}


def show_graph_with_labels(adjacency_matrix, nodes):
    df = pd.DataFrame(adjacency_matrix, index=nodes, columns=nodes)
    G = nx.from_pandas_adjacency(df, create_using=nx.DiGraph)
    layout = nx.spring_layout(G)
    # nx.draw_networkx_edge_labels(G, layout)
    nx.draw(G, layout, with_labels=True, arrowstyle='-|>')
    plt.show()


if __name__ == "__main__":
    show_graph_with_labels(trans_matrix, nodes)

