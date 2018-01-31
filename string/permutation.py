__author__ = 'jellyzhang'

'''
全排列
'''

arr=[1,2,3]

#列表输出
def show(a):
    print(a)

#交换
def swap(a,i,j):
    tmp=a[i]
    a[i]=a[j]
    a[j]=tmp

#全排列递归
def permutation(a,begin,end):
    if begin>=end:
        show(a)
    else:
        for j in range(begin,end):
            swap(a,begin,j)
            permutation(a,begin+1,end)
            swap(a,begin,j)





permutation(arr,0,3)