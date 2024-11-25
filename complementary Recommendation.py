import pandas as pd
import networkx as nx
import community as community_louvain
from collections import defaultdict
from HG.Recommendations import communities

file_path_community = 'product_network.csv'
data_community = pd.read_csv(file_path_community)
file_path_elasticity = 'cross_price_elasticity_result.csv'
data_elasticity = pd.read_csv(file_path_elasticity)
G = nx.Graph()
for _, row in data_community.iterrows():
    G.add_edge(row['product.index'], row['product.neighbor.index'])
partition = community_louvain.best_partition(G)
product_to_community = {product: community for product, community in partition.items()}
community_cross_elasticity_recommendations = defaultdict(list)

for comm, products in communities.items():
    for product1, product2 in product_pairs:
        community_cross_elasticity_recommendations[comm].append((product1, product2))
for comm, recs in community_cross_elasticity_recommendations.items():
    print(f"Community {comm}: Complementary product recommendations {recs}")
