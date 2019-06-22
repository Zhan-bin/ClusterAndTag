import numpy as np
import pandas as pd
import random
def get(path="data/u.data"):
    prefer = []
    uid_max=0
    mid_max=0
    for line in open(path, 'r'):  # 打开指定文件
        (userid, movieid, rating, ts) = line.split('\t')  # 数据集中每行有4项
        uid = int(userid)
        mid = int(movieid)
        rat = float(rating)
        if(uid>uid_max):
            uid_max=uid
        if(mid>mid_max):
            mid_max=mid
        prefer.append([uid, mid, rat])
    matrix = [[0 for col in range(mid_max+1)] for row in range(uid_max+1)]
    for l in prefer:
        matrix[l[0]][l[1]] = l[2]
    np.savetxt("data/R.txt",matrix)
    print(uid_max,mid_max)