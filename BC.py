import networkx as nx
import os
import operator
import numpy as np
import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns
from collections import Counter, defaultdict
from prettytable import PrettyTable
import pylab
import community
dataset_path = os.path.join(os.getcwd(), r"..\datasets")
#print(dataset_path)
os.listdir(dataset_path)
prod_path = os.path.join(dataset_path, "product.csv")
prod_df = pd.read_csv(prod_path, encoding = 'unicode_escape')
#prod_df.head(5)
network_df = pd.read_csv(prod_path, encoding = 'unicode_escape')
#network_df.head(5)
prod_df[prod_df["salesrank"]==-1]
prod_df = prod_df[prod_df["salesrank"] != -1]
prod_df["salesrank"].min(), prod_df["salesrank"].max()
SALESRANK_TOP = 100000

books_df = prod_df[
    (prod_df["group"] == "Book") &
    (prod_df["salesrank"] <= SALESRANK_TOP)
]
books_df.rating.min(), books_df.rating.max()
books_df.rating.value_counts()
network_books_df = network_df[
    network_df.source.isin(books_df.id) &
    network_df.destination.isin(books_df.id)
]
network_book_indegree = network_books_df.groupby(['destination'])['source'].size().reset_index(name='in_degree')
network_book_outdegree = network_books_df.groupby(['source'])['destination'].size().reset_index(name='out_degree')
network_book_indegree["in_degree"].min(), network_book_indegree["in_degree"].max()
network_book_outdegree["out_degree"].min(), network_book_outdegree["out_degree"].max()
temp_1 = network_book_outdegree.set_index('source')
temp_2 = network_book_indegree.set_index('destination').rename_axis('source')
temp_2.columns = temp_1.columns

merged = temp_2.add(temp_1, fill_value=0).loc[temp_2.index, :].reset_index()
merged.nlargest(5, 'out_degree')
for row in merged.nlargest(5, 'out_degree').iterrows():
    # print(row[1].source)
    title = prod_df[prod_df['id'] == int(row[1].source)]
    print(f"Title: {title.iat[0,1]}")
    print(f"Outdegree: {row[1].out_degree}")
    print("#-----------------------------")
network_final_df = network_books_df.groupby(['source', 'destination']).size().reset_index(name='occurance')
network_final_df.head()
nx_graph = nx.from_pandas_edgelist(
    network_final_df, 'source', 'destination', ['occurance']
)
num_nodes = nx_graph.number_of_nodes()
num_edges = nx_graph.number_of_edges()
nx.is_connected(nx_graph)
nx.density(nx_graph)
num_connected_comps = nx.number_connected_components(nx_graph)
dc = nx.degree_centrality(nx_graph)
sorted_dc = sorted(dc.items(), key=operator.itemgetter(1), reverse=True)
x = PrettyTable()
x.field_names = ["Attribute", "Node", "Centrality Value"]

x.add_row(["Highest Degree Centrality", sorted_dc[0][0], sorted_dc[0][1]])
print(x)
degree_sequence = sorted(dict(nx.degree(nx_graph)).values(), reverse=True)
plt.figure(figsize=(10,7))
plt.loglog(degree_sequence, 'b-', marker='o')
plt.title('Degree Rank Plot')
plt.ylabel('Degree')
plt.xlabel('Rank')
plt.grid()
plt.show()