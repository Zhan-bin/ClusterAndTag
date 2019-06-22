from sklearn.cluster import KMeans
import numpy as np

class cluster:
    def __init__(self,data_path = "data/sim_u.txt",cluster_num = 10,KNN_K = 20):
        self.data_path = data_path
        self.cluster_num = cluster_num
        self.KNN_K = KNN_K

    def clusterByFile(self):
        """
        读取numpy存取的矩阵文件转换为相似度矩阵再进行聚类
        :return:
        """
        sim_matrix = np.loadtxt(self.data_path)[1:, 1:]
        self.clusterByMatrix(sim_matrix)

    def getW(self,sim_matrix):
        """
        利用KNN获得相似矩阵
        :param data: 样本集合
        :param k: KNN参数
        :return:
        """
        W = np.zeros((sim_matrix.shape[0], sim_matrix.shape[0]))
        for idx, each in enumerate(sim_matrix):
            index_array = np.argsort(each)[::-1]
            W[idx][index_array[1:self.KNN_K + 1]] = 1
        tmp_W = np.transpose(W)
        W = (tmp_W + W) / 2
        return W

    def getD(self,W):
        """
        获得度矩阵
        :param W:  相似度矩阵
        :return:   度矩阵
        """
        D = np.diag(np.sum(W, axis=1))
        return D

    def getL(self,D, W):
        """
        获得拉普拉斯举着
        :param W: 相似度矩阵
        :param D: 度矩阵
        :return: 拉普拉斯矩阵
        """
        return D - W

    def getEigen(self,L):
        """
        从拉普拉斯矩阵获得特征矩阵
        :param L: 拉普拉斯矩阵
        :return:
        """
        eigval, eigvec = np.linalg.eig(L)
        ix = np.argsort(eigval)[0:self.cluster_num]
        return eigvec[:, ix]

    def clusterByMatrix(self,sim_matrix):
        """
        根据相似度矩阵进行聚类并保存中间数据
        文件命名规则： D _ cluster_num _ KNN_K
        """
        W = self.getW(sim_matrix)
        D = self.getD(W)
        L = self.getL(D, W)
        np.savetxt("data/cluster/D_"+str(self.cluster_num)+"_"+str(self.KNN_K)+".txt", D)
        np.savetxt("data/cluster/W_"+str(self.cluster_num)+"_"+str(self.KNN_K)+".txt", W)
        np.savetxt("data/cluster/L_"+str(self.cluster_num)+"_"+str(self.KNN_K)+".txt", L)
        eigvec = self.getEigen(L)
        clf = KMeans(n_clusters=self.cluster_num)
        s = clf.fit(eigvec)
        C = s.labels_
        np.savetxt("data/cluster/C_"+str(self.cluster_num)+"_" +str(self.KNN_K)+".txt",C)
        print("聚类结果："+str(C))

    def setConfig(self,cluster_num,KNN_K):
        self.cluster_num = cluster_num
        self.KNN_K = KNN_K
