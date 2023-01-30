import networkx as nx
import matplotlib.pyplot as plt
from map import cities

g = nx.Graph()
for edge in edgelist:
    g.add_edge(edge[0], edge[1], weight = edge[2])



pos = nx.spring_layout(g)
nx.draw_networkx(g, pos)
plt.title("Cities` distance")
plt.show()

print(nx.shortest_path(g, '', '', weight = 'weight'))