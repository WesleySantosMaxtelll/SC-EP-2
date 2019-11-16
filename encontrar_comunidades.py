import community as commu
import networkx as nx
import matplotlib.pyplot as plt


def cria_comundades(nodes_hash_dict):
    # Replace this with your networkx graph loading depending on your format !
    # G = nx.erdos_renyi_graph(30, 0.05)
    G = nx.Graph()
    nodes = list(nodes_hash_dict)
    G.add_nodes_from(nodes)


    conexoes = []
    for node in nodes_hash_dict:
        for d_node in nodes_hash_dict[node]:
            # for _ in range(nodes_hash_dict[node][d_node]):
            conexoes.append((node, d_node))
    G.add_edges_from(conexoes)

    # first compute the best partition
    partition = commu.best_partition(G)

    # drawing
    size = float(len(set(partition.values())))
    pos = nx.spring_layout(G)
    count = 0
    for com in set(partition.values()):
        count = count + 1.
        list_nodes = [nodes for nodes in partition.keys()
                      if partition[nodes] == com]
        nx.draw_networkx_nodes(G, pos, list_nodes, node_size=20,
                               node_color=str(count / size))

    nx.draw_networkx_edges(G, pos, alpha=0.5)
    plt.show()
    return partition


def devolve_label(partition, datas, valores):
    pass