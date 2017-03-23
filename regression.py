# coding=utf-8

import numpy as np
import matplotlib.pyplot as plt

def file2matrix(filename):
    with open(filename) as f:
        contents = f.readlines()
        length = len(contents) # 得到文件内容的行数
        Mat = np.zeros((length, 3)) # 创建一个空矩阵用于存储文件内容
        index = 0
        for line in contents:
            line = line.strip() # 去除每一行的换行符
            data = line.split('\t')
            Mat[index, :] = data # 将每一列数据按照行索引存放到空矩阵
            index += 1
            
    return np.mat(Mat)

def my_scatter(dataMat):
    x = dataMat[:, 1]
    y = dataMat[:, 2]
    plt.xlabel('x')
    plt.ylabel('y')
    #plt.plot(x, y)  # line
    plt.plot(x, y, 'o') # circle marker => scatter
    plt.show()

    
data_file = "C:\Users\chen\Documents\GitHub\python_ml\data.txt"
dataMat = file2matrix(data_file)
# print dataMat[:, 1]
my_scatter(dataMat)
