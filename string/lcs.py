__author__ = 'jellyzhang'
'''
最长公共子序列(LCS)
'''
import numpy as np
from 栈.stack import *
def getLCS(str1,str2):
    len1=len(str1)
    len2=len(str2)

    if len1==0 or len2==0:
        return 0
    else:
        data = np.zeros(shape=(len1 + 1, len2 + 1), dtype=np.int)
        for index1,s1 in enumerate(str1):
            for index2,s2 in enumerate(str2):
                if s1==s2:
                    data[index1+1][index2+1]=data[index1][index2]+1
                else:
                    data[index1+1][index2+1]=max(data[index1+1][index2],data[index1][index2+1])

        #输出最大匹配子序列
        i=len1;j=len2;
        stack=Stack()
        while i>0 and j>0:
            if str1[i-1]==str2[j-1]:
                stack.push(str1[i-1])
                i-=1
                j-=1
            else:  #不等时选择对应位置
                if data[i][j-1]<=data[i-1][j]:
                    i-=1
                else:
                    j-=1
        cls=''
        while not stack.isEmpty():
            cls+=stack.pop()
        return data[len1][len2],cls


print(getLCS('ABCBDAB','BDCABA'))

