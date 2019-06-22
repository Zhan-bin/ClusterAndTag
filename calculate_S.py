import numpy as np

def calSim_user(R,num_user):   #计算所有用户的相似度
    sim_user = [[0 for col in range(num_user+1)] for row in range(num_user+1)]
    for i in range(1,num_user+1):
        for j in range(i,num_user+1):
            sim_user[i][j] = sim_user[j][i] = cosSim(R[i],R[j])
    print(sim_user)
    np.savetxt("data/sim_u.txt",sim_user)

def calSim_ClusterAndUser(R,H):    #计算用户与类别之间的相似度
    num_user = R.shape[0]-1
    num_cluster = H.shape[0]
    sim_clu_user = [[0 for col in range(num_cluster)] for row in range(num_user+1)]
    for i in range(1,num_user+1):
        for j in range(0,num_cluster):
            sim_clu_user[i][j]= cosSim(R[i],H[j])
    print(sim_clu_user)
    np.savetxt("data/C.txt",sim_clu_user)
    return sim_clu_user

def cosSim(v1,v2): #余弦相似度计算
    v1_v2 = 0
    fv1 = 0
    fv2 = 0
    for i in range(1,len(v1)):
            v1_v2 += v1[i]*v2[i]
            fv1 += (v1[i]**2)
            fv2 += (v2[i]**2)
    if (fv1**0.5)*(fv2**0.5) == 0:
        return 0
    result = v1_v2/((fv1**0.5)*(fv2**0.5))
    result = int(result*1000+0.5)/1000
    return result
