import pandas as pd
import networkx as nx
import community as community_louvain
from collections import defaultdict


file_path_community = 'product_network.csv'
data_community = pd.read_csv(file_path_community)


file_path_recommendation = 'clean_amazon.csv'
data_recommendation = pd.read_csv(file_path_recommendation)


G = nx.Graph()
for _, row in data_community.iterrows():
    G.add_edge(row['product.index'], row['product.neighbor.index'])

partition = community_louvain.best_partition(G)

communities = defaultdict(list)
for product, comm in partition.items():
    communities[comm].append(product)

recommendations = defaultdict(list)
for _, row in data_recommendation.iterrows():
    recommendations[row['FromNodeId']].append(row['ToNodeId'])

community_recommendations = defaultdict(list)
for comm, products in communities.items():
    for product in products:
        if product in recommendations:
            community_recommendations[comm].extend(recommendations[product])

for comm, recs in community_recommendations.items():
    print(f"Community {comm}: Recommended products {set(recs)}")
