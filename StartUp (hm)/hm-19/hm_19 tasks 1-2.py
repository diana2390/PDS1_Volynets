import networkx as nx
import matplotlib.pyplot as plt
from map import cities

def cities_path(graph, city_1, city_2, weight='weight'):
    path = nx.shortest_path(graph, city_1, city_2, weight)
    length = nx.shortest_path_length(graph, city_1, city_2, weight)
    return print(f"The shortest way from {city_1} to {city_2} is {path}.\n The length between cities is {length} km.")

g = nx.Graph()
for edge in cities:
    g.add_edge(edge[0], edge[1], weight=int(edge[2]))

pos = nx.spring_layout(g)
nx.draw_networkx(g, pos)
plt.title("Cities` distance")
plt.show()

cities_path(g,'Radomyshl', 'Myrhorod', weight='weight')
cities_path(g, 'Lubny', 'Radomyshl', weight='weight')