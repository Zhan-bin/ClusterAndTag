import numpy as np
from spectral import cluster
import calculate_S
import calculate_H
import calculate_C
import getRatingMatrix
import spectral
if __name__ == '__main__':
    # getRatingMatrix.get()
    # R = np.loadtxt("data/R.txt")
    # num_user = R.shape[0]-1
    # num_item = R.shape[1]-1
    # calculateSim.calSim_user(R,num_user)
    # clu = cluster()
    # clu.clusterByFile()
    # clusterPrefer = calculate_H.\
    #     calculateClusterPrefer("data/R.txt",
    #                            "data/cluster/C_"+str(clu.cluster_num)+"_"+str(clu.KNN_K)+".txt",
    #                            "data/sim_u.txt",
    #                            clu.cluster_num)
    # clusterPrefer.prefer_all()
    getC = calculate_C.calculate_C("data/R.txt","data/H.txt")
    getC.calculate()