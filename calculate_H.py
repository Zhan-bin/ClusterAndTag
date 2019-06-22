import numpy as np
import copy
class calculateClusterPrefer:
    def __init__(self,path_R,path_C,path_simU,num_cluster):
        self.num_cluster = num_cluster
        self.R = np.loadtxt(path_R)[1:]
        self.C = np.loadtxt(path_C)
        self.sim_u = np.loadtxt(path_simU)[1:,1:]
        print("相似度矩阵：")
        print(self.sim_u)
        self.index = []
        for i in range(self.num_cluster):
            id = []
            for j in range(self.C.shape[0]):
                if(self.C[j]==i):
                    id.append(j)
            self.index.append(id)
        print("index:")
        print(self.index)

    def prefer_item(self,col_item):
        num = col_item.shape[0]
        zeroCount = 0
        sum = 0
        for i in range(num):
            if(col_item[i]==0):
                zeroCount+=1
            else:
                sum += col_item[i]
        if(zeroCount == num):
            return 0
        else:
            return ( sum/(num-zeroCount) ) * zeroCount + sum

    def prefer_clu(self,clu_matrix,cluId):
        prefer = [0]
        print("类别"+str(cluId))
        print(clu_matrix)
        for i in range(clu_matrix.shape[1]):
            col_item = self.fill(clu_matrix[:,i], cluId)
            prefer.append(self.prefer_item(col_item))
        return prefer

    def prefer_all(self):
        H=[]
        for i in range(self.num_cluster):
            prefer_c = []
            for j in range(self.C.shape[0]):
                if(self.C[j]==i):
                    prefer_c.append(self.R[j,:])
            H.append(self.prefer_clu(np.array(prefer_c),i))
        np.savetxt("data/H.txt",H)
        print("H矩阵:"+str(len(H[0])))
        print(H)
        return H

    def fill(self,col_item,cluId):
        col_item_fill = copy.deepcopy(col_item)
        for i in range(len(col_item)):
            if(col_item[i]==0):
                s=0
                s_r=0
                for j in range(len(col_item)):
                    if(col_item[j]!=0):
                        sim = self.sim_u[self.index[cluId][i]][self.index[cluId][j]]
                        s+=sim
                        s_r+=(sim*col_item[j])
                if(s==0):
                    col_item_fill[i]=0
                else:
                    col_item_fill[i]=int(((s_r/s)*10)+0.5) /10
        return np.array(col_item_fill)