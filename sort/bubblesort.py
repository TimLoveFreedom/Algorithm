__author__ = 'jellyzhang'
'''
冒泡排序
原理：将序列划分为无序和有序区，不断通过交换较大元素至无序区尾完成排序
'''
def bubblesort(a):
    for i in range(len(a)-1):
        for j in range(len(a)-1-i):
            if a[j]>a[j+1]:
                tmp=a[j]
                a[j]=a[j+1]
                a[j+1]=tmp
    return a
print(bubblesort([10,2,15,30,20]))