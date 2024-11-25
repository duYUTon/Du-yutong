import torch
import torch.nn.functional as F
from torch.nn import GCNConv, GATConv
class HAN(torch.nn.Module):
    def __init__(self, num_users, num_products, embedding_dim, num_han_layers, dropout_rate):
        super(HAN, self).__init__()
        self.num_users = num_users
        self.num_products = num_products
        self.embedding_dim = embedding_dim
        self.num_han_layers = num_han_layers
        self.dropout_rate = dropout_rate

        self.user_embedding = torch.nn.Embedding(num_users, embedding_dim)
        self.product_embedding = torch.nn.Embedding(num_products, embedding_dim)

        self.han_layers = torch.nn.ModuleList([
            HANLayer(embedding_dim, dropout_rate)
            for _ in range(num_han_layers)
        ])

        self.out = torch.nn.Linear(embedding_dim, num_products)

    def forward(self, user_ids, product_ids):
        user_embeddings = self.user_embedding(user_ids)
        product_embeddings = self.product_embedding(product_ids)

        for layer in self.han_layers:
            user_embeddings, product_embeddings = layer(user_embeddings, product_embeddings)
        combined_embeddings = torch.cat([user_embeddings, product_embeddings], dim=1)
        product_embeddings = self.out(combined_embeddings)
        product_embeddings = F.softmax(product_embeddings, dim=1)
        return product_embeddings
class HANLayer(torch.nn.Module):
    def __init__(self, embedding_dim, dropout_rate):
        super(HANLayer, self).__init__()
        self.user_conv = GCNConv(embedding_dim, embedding_dim)
        self.product_conv = GCNConv(embedding_dim, embedding_dim)
        self.dropout = torch.nn.Dropout(dropout_rate)

    def forward(self, user_embeddings, product_embeddings):
        # Aggregate information from neighbors for users
        user_embeddings = self.dropout(self.user_conv(user_embeddings, product_embeddings))

        # Aggregate information from neighbors for products
        product_embeddings = self.dropout(self.product_conv(product_embeddings, user_embeddings))

        return user_embeddings, product_embeddings



num_users = 1000
num_products = 1000
embedding_dim = 128
num_han_layers = 2
dropout_rate = 0.5

model = HAN(num_users, num_products, embedding_dim, num_han_layers, dropout_rate)


user_ids = torch.randint(0, num_users, (100,))
product_ids = torch.randint(0, num_products, (100,))


product_embeddings = model(user_ids, product_ids)
