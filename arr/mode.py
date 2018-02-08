__author__ = 'jellyzhang'

'''
绝对众数
'''


def mode(arr):
    m=0
    c=0
    for a in arr:
        if c==0:
            m=a
            c=1
        elif a==m:
            c+=1
        else:
            c-=1
    return m



a=[1,2,2,2,3,4,2]
print(mode(a))