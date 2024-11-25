# Du-yutong
Research on personalized recommendation of complementary products based on demand cross-elasticity and hypergraphs
A personalized recommendation model called Hg-CR, which is based on demand cross-elasticity and hypergraphs, aims to improve the utility and accuracy of recommendation systems and help users make more informed shopping decisions.
The core idea of the model:
(1) Using cross-elasticity theory to explore the relationship between complementary products: Unlike the existing methods that consider “co-purchase” as an indicator of complementarity, the Hg-CR model utilizes the theory of cross elasticity of demand to more accurately identify complementary products by analyzing the price of goods and users' purchasing behaviors.
(2) Hypergraph combining social and product relationships: The model represents users, items and social relationships as nodes, and their interactions and associations as hyperedges, thus better capturing the complex higher-order relationships between users and items.
(3) Community Detection to Improve Recommendation Accuracy: The model uses a community detection algorithm to group users with similar interests to provide more accurate recommendations within the same community.
(4) Recommendation based on similarity and complementarity: Within each community, the model makes product recommendations based on user similarity and complementarity to provide users with a more personalized shopping experience.
Data and code descriptions:
CODE：
（1）Data.ipynb: Data analysis and visualization of the amazon-meta.txt dataset, read the “amazon-meta.txt” file, cleaned the data and saved it as “Amazon_clean_meta.txt”. And a network diagram was created to represent the relationship between these products. 
（2）Cross Price Elasticity of Demand.py: Calculates the cross price elasticity between two products by reading product data. 
（3）HAN.py: Learning embedded representations of users and products by hierarchically aggregating neighbor information between them. 
（4）BC.py: performs network analysis, including data loading, processing, network graph construction, community detection and visualization.
（5）P4.py: Construct a network graph, use Louvain's method for community discovery, color each node by the community it belongs to, and finally display the network graph visually. 
（6）Recommendations.py: By analyzing product network data and recommendation data, it identifies the community to which the product belongs and generates a list of recommended products based on the community structure. 
（7）complementary Recommendation.py: By analyzing product network data and price elasticity data, it identifies the community to which the product belongs and generates a list of complementary product recommendations based on the community structure.
DATA：
（1）amazon-meta.txt: data downloaded from SNAP.
（2）product.csv: contains all product information.
（3）amazon_clean_meta.txt: dataset after data processing.
（4）product_network.csv: each row in the dataset represents a product (product.index) and its neighboring products (product.neighbor.index)
