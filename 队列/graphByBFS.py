__author__ = 'jellyzhang'
'''
无向图最短路径条数
(1-15一共多少条最短路径；连通则边为1)
'''
import numpy as np
import  queue
q=queue.Queue()
# 初始化数据
def init_data():
    data = np.zeros((16, 16))
    data[0][1]=data[0][4]=1
    data[1][5]=data[1][0]=data[1][2]=1
    data[2][1]=data[2][6]=data[2][3]=1
    data[3][2]=data[3][7]=1
    data[4][0]=data[4][5]=1
    data[5][1]=data[5][4]=data[5][6]=data[5][9]=1
    data[6][2]=data[6][5]=data[6][7]=data[6][10]=1
    data[7][3]=data[7][6]=1
    data[8][9]=data[8][12]=1
    data[9][8]=data[9][13]=data[9][10]=1
    data[10][9]=data[10][14]=data[10][11]=1
    data[11][10]=data[11][15]=1
    data[12][8]=data[12][13]=1
    data[13][9]=data[13][12]=data[13][14]=1
    data[14][10]=data[14][13]=data[14][15]=1
    data[15][11]=data[15][14]=1
    return data

#计算
N=16
def cal(data):
    print(data)
    steps=np.zeros(16) #每个节点第几步可以到达
    stepNumber=np.zeros(16) #到每种节点有几种走法
    stepNumber[0]=1
    q.put(0)  #起始节点入队
    while  not q.empty():
        start=q.get()
        s=steps[start]+1

        for i in range(1,N):
            if data[start][i]==1:  #连通
                if steps[i]==0 or steps[i]>s: #i尚未可达或者发现更短的路
                    steps[i]=s
                    stepNumber[i]=stepNumber[start]
                    q.put(i)
                elif steps[i]==s: #发现相同长度路径
                    stepNumber[i]+=stepNumber[start]
    return stepNumber[N-1]


print(cal(init_data()))