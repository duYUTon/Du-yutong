import pandas as pd
import networkx as nx
import community as community_louvain
import matplotlib.pyplot as plt

data = pd.read_csv('product_network.csv')

G = nx.Graph()

for index, row in data.iterrows():
    node = row['product.index']
    neighbors = str(row['product.neighbor.index']).split()
    for neighbor in neighbors:
        if neighbor != node:
            G.add_edge(node, neighbor)

partition = community_louvain.best_partition(G)

for node, community in partition.items():
    print(f'Node {node} is in community {community}')

pos = nx.spring_layout(G)
plt.figure(figsize=(12, 12))
plt.axis('off')
colors = [partition[node] for node in G.nodes()]

nx.draw_networkx_nodes(G, pos, node_color=colors, node_size=20)
nx.draw_networkx_edges(G, pos, alpha=0.5)
plt.show()