import calculate_S
import numpy as np
class calculate_C:
    def __init__(self,path_R,path_H):
        self.R = np.loadtxt(path_R)   #用户编号从1到num_user
        self.H = np.loadtxt(path_H) #类别编号从0到 num_cluster-1

    def calculate(self):
        return calculate_S.calSim_ClusterAndUser(self.R, self.H)