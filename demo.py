import calculate_S
import calculate_C
import calculate_H
import spectral
import numpy as np
import getRatingMatrix

if __name__ == '__main__':
    # sim_matrix = np.array([[1, 0.8, 0.7, 0.1, 0, 0], [0.8, 1, 0.6, 0, 0, 0],
    #           [0.7, 0.6, 1, 0, 0.2, 0], [0.1, 0, 0, 1, 0.7, 0.7],
    #           [0, 0, 0.2, 0.7, 1, 0.9], [0, 0, 0, 0.7, 0.9, 1]])
    # clu = spectral.cluster()
    # clu.setConfig(2,3)
    # clu.clusterByMatrix(sim_matrix)

    R = np.array([[0, 0, 0],
                  [1, 0, 1], [2, 4, 0], [1, 2, 3],
                  [5, 1, 0], [0, 5, 1], [0, 0, 5]])
    # np.savetxt("data/R.txt",R)
    # # calculate_S.calSim_user(R,6)
    # clu = spectral.cluster()
    # clu.setConfig(2,3)
    # clu.clusterByMatrix(np.loadtxt("data/sim_u.txt")[1:,1:])
    # ch = calculate_H.calculateClusterPrefer("data/R.txt","data/cluster/C_2_3.txt","data/sim_u.txt",2)
    # ch.prefer_all()
    H = np.loadtxt("data/H.txt")
    calculate_S.calSim_ClusterAndUser(R,H)