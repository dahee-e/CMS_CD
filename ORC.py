import networkx as nx
import time

from GraphRicciCurvature.FormanRicci import FormanRicci
from GraphRicciCurvature.OllivierRicci import OllivierRicci

print("\n- Import an example NetworkX karate club graph")
G = nx.read_edgelist("dataset/polblogs/network.dat",nodetype=int)

start_time = time.time()
print("\n===== Compute the Ollivier-Ricci curvature of the given graph G =====")
# compute the Ollivier-Ricci curvature of the given graph G
orc = OllivierRicci(G, alpha=0.5, verbose="INFO")
orc.compute_ricci_curvature()

end_time = time.time()
print("Time: %s seconds" % (end_time - start_time))

# get the edge in network
edge1, edge2 = list(G.edges())[0][1], list(G.edges())[0][0]
print(f"Karate Club Graph: The Ollivier-Ricci curvature of edge ({edge1},{edge2}) is %f" % orc.G[edge1][edge2]["ricciCurvature"] )



