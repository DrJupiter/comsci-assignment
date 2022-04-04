
from copy import deepcopy
import numpy as np
import networkx as nx
import matplotlib.pyplot as plt


G = nx.karate_club_graph()
# nx.draw(G)
# print(nx.adjacency_matrix(G).todense())


## A
C = G

## B
N = 0

def double_edge_swap(G, N):
    Gp = G.copy()
    for i in range(N):
        E  = np.array(list(Gp.edges()))
        r = np.random.randint(len(E),size=(2,))
        u, v = E[r[0]] 
        x, y = E[r[1]]
        if u != v and v!= x:
            if Gp.has_edge(u,y) or Gp.has_edge(x,v):
                continue
            else:
                Gp.remove_edge(u,v)
                Gp.remove_edge(x,y)
                Gp.add_edge(u,y)
                Gp.add_edge(x,v)
    return Gp

B = double_edge_swap(G, 20)

# nx.draw(B)

# nx.draw(G)


# print(G.degree())
# print(B.degree())