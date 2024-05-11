import networkx as nx

G = nx.Graph()

people = ["Anna", "Bob", "Ivan", "Diana", "Edward", "Fiona", "George", "Helen", "Ivan", "Julia"]


G.add_nodes_from(people)


friendships = [("Anna", "Bob"), ("Anna", "Diana"), ("Bob", "Ivan"), ("Ivan", "Diana"),
               ("Diana", "Edward"), ("Edward", "Fiona"), ("Fiona", "George"), ("George", "Helen"),
               ("Helen", "Ivan"), ("Ivan", "Julia"), ("Julia", "Anna"), ("Bob", "Edward"),
               ("Ivan", "Fiona"), ("Diana", "Helen"), ("Edward", "Ivan")]


G.add_edges_from(friendships)


dfs_path = list(nx.dfs_edges(G, source="Anna"))


bfs_path = list(nx.bfs_edges(G, source="Anna"))

dfs_path, bfs_path

def print_path(algorithm_name, path):
    print(f"{algorithm_name} Path:")
    for start, end in path:
        print(f"{start} -> {end}")
    print() 


print_path("DFS", dfs_path)
print_path("BFS", bfs_path)
