__author__ = 'jellyzhang'
'''
kmp算法
'''
import  numpy as np
text="ABCDABCEAAAABASABCDABCADABCDABCEAABCDABCEAAABASABCDABCAABLAKABCDABABCDABCEAAADSFDABCADABCDABCEAAABCDABCEAAABASABCDABCADABCDABCEAAABLAKABLAKK"
s="ABCDABCEAAABASABCDABCADABCDABCEAAABLAK"
#暴力破解法
def brute_force(text,s):
    sLen=len(s)
    tEnd=len(text)-sLen
    for start in range(tEnd):
        if text[start:start+sLen]==s:
            return start
    return -1

print('***********************************')
print('暴力破解返回匹配位置：{}'.format(brute_force(text,s)))
print('***********************************')




#next数组
def getNext(p):
    next=np.zeros(len(p),dtype=int)
    next[0]=-1
    k=-1 #next[j]
    j=0
    while j<(len(p)-1):
        if k==-1 or p[j]==p[k]: #求j+1
            j+=1
            k+=1
            next[j]=k
        else:
            k=next[k]
    return  next

print('***********************************')
print('next数组测试：{}'.format(getNext('ABABA')))
print('***********************************')



#kmp
def kmp(text,s):
    ans=-1
    i=0;j=0
    tLen=len(text)
    pLen=len(s)
    while i<tLen:
        if j==-1 or text[i]==s[j]:
            i+=1
            j+=1
        else:
            j=getNext(s)[j]
        if j==pLen:
            ans= i-pLen
            break
    return  ans
print('***********************************')
print('kmp返回匹配位置：{}'.format(kmp(text,s)))
print('***********************************')



