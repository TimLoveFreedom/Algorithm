__author__ = 'jellyzhang'
'''
插入排序
原理：将数组分为有序和无序区，然后不断将无序区的第一个元素按大小插入到有序区中，最终将所有无序区元素都移动到有序区完成排序
'''
def insertsort(a):
    for i in range(1,len(a)):
        tmp=a[i]
        j=i-1
        while j>=0:
            if tmp<a[j]:
                a[j+1]=a[j]
            else:
                break
            j-=1
        a[j+1]=tmp

    return  a

print(insertsort([10,2,14,8,20,16,30]))