from sklearn.cluster import KMeans
import numpy as np
import calculate_S
# import math as m
import copy
import matplotlib.pyplot as plt
import numpy as np
# i2=np.array([0,1])
# i3=np.array([1,0])

v2=np.array([[0,1,2],[2,2,2]])
# v3=np.array([[1,2,3],[2,2,2]])
# print(np.multiply(v2[i2,:],v3[i3,:]))
# file = open("data/u.data")
# a=[[1,2],[3,4],[5,6]]
# df = pd.DataFrame(a)
# out = df.values
# a=np.array([1,2,3,4,5,6,7,8])
b=[[1,2,3],[4,5,6]]
# np.savetxt("data/a.txt",b)
# print(np.loadtxt("data/a.txt"))

# import networkx as nx
# import matplotlib.pyplot as plt
# sim_u = np.loadtxt("data/sim_u.txt")
# G=nx.Graph()
# G.add_nodes_from(range(1,4))
# edglist=[]
# for i in range(1,944):
#     for j in range(i+1,944):
#         if(sim_u[i][j]!=0):
#             edglist.append((i,j,sim_u[i][j]))
#
# G=nx.Graph()
# G.add_weighted_edges_from(edglist)
# position = nx.circular_layout(G)
# nx.draw_networkx_nodes(G,position, nodelist=range(1,4), node_color="r")
# nx.draw_networkx_edges(G,position)
# nx.draw_networkx_labels(G,position)
# # nx.draw(G,nodelist=[1,2,3])
# plt.show()
q=1.35*10+0.5
print(q)
print(int(q)/10)
