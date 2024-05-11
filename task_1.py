import networkx as nx
import matplotlib.pyplot as plt

G = nx.Graph()


people = ["Anna", "Bob", "Ivan", "Diana", "Edward", "Fiona", "George", "Helen", "Ivan", "Julia"]


G.add_nodes_from(people)


friendships = [("Anna", "Bob"), ("Anna", "Diana"), ("Bob", "Ivan"), ("Ivan", "Diana"),
               ("Diana", "Edward"), ("Edward", "Fiona"), ("Fiona", "George"), ("George", "Helen"),
               ("Helen", "Ivan"), ("Ivan", "Julia"), ("Julia", "Anna"), ("Bob", "Edward"),
               ("Ivan", "Fiona"), ("Diana", "Helen"), ("Edward", "Ivan")]


G.add_edges_from(friendships)


plt.figure(figsize=(10, 8))
nx.draw(G, with_labels=True, node_color='lightblue', edge_color='gray', node_size=2000, font_size=10, font_weight='bold')
plt.title("Модель соціальної мережі")
plt.show()


node_count = G.number_of_nodes()
edge_count = G.number_of_edges()
degrees = dict(G.degree())

node_count, edge_count, degrees
