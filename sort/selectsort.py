__author__ = 'jellyzhang'
'''
简单选择排序
原理：将序列划分为无序和有序区，寻找无序区中的最小值和无序区的首元素交换，有序区扩大一个，循环最终完成全部排序
'''
def quicksort(a):
    for i in range(len(a)):
        for j in range(i+1,len(a)):
            if a[i]>a[j]:
                tmp=a[i]
                a[i]=a[j]
                a[j]=tmp
    return  a

print(quicksort([10,2,20,5,14]))