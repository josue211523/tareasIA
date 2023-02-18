import casos as c
import networkx as nx
import matplotlib.pyplot as plt
 
#Networkx grafo generado como imagen
G = nx.Graph() 

# camino del caso
caminos = c.caminos1

G.add_weighted_edges_from(caminos)
pos=nx.spring_layout(G)
nx.draw(G, pos, with_labels=True, font_weight='bold')
edge_weight = nx.get_edge_attributes(G,'weight')
nx.draw_networkx_edge_labels(G, pos, edge_labels = edge_weight)
plt.show() 

# nombre de la imagen
plt.savefig('grafo1.png') 