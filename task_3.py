import networkx as nx


G_weighted = nx.Graph()


people = ["Anna", "Bob", "Ivan", "Diana", "Edward", "Fiona", "George", "Helen", "Ivan", "Julia"]


friendships_weighted = [("Anna", "Bob", 2), ("Anna", "Diana", 4), ("Bob", "Ivan", 1),
                        ("Ivan", "Diana", 3), ("Diana", "Edward", 2), ("Edward", "Fiona", 4),
                        ("Fiona", "George", 3), ("George", "Helen", 2), ("Helen", "Ivan", 1),
                        ("Ivan", "Julia", 3), ("Julia", "Anna", 1), ("Bob", "Edward", 5),
                        ("Ivan", "Fiona", 2), ("Diana", "Helen", 1), ("Edward", "Ivan", 4)]


for (u, v, w) in friendships_weighted:
    G_weighted.add_edge(u, v, weight=w)


dijkstra_path = nx.single_source_dijkstra_path(G_weighted, source="Anna")

dijkstra_path

def print_dijkstra_paths(paths):
    print("Найкоротші шляхи від Anna до інших вершин:")
    for target, path in paths.items():

        total_weight = sum(G_weighted[u][v]['weight'] for u, v in zip(path[:-1], path[1:]))

        formatted_path = " → ".join(path)
        print(f"Шлях від Anna до {target}:\n- Шлях: {formatted_path}\n- Загальна вага: {total_weight}\n")


print_dijkstra_paths(dijkstra_path)
