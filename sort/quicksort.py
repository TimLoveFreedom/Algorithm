__author__ = 'jellyzhang'
'''
快速排序
算法描述：
快速排序使用分治法策略来吧一个序列分为两个子序列
1、从数列中挑出一个元素，称为‘基准’（pivot）
2、重新排序数列，所有比基准值小的元素排在基准前面；所有比基准大的元素排在基准后面。在这个分区结束之后，该基准就处于数列的中间位置（分区操作）
3、递归地把小于基准值元素的子数列和大于基准值元素的子数列排序
'''
def quicksort(a):
    less=[]
    greater=[]
    if len(a)<=1:
        return  a
    else:
        pivot=a[-1]  #基准
        for v in a[:-1]:
            if v <=pivot:
                less.append(v)
            else:
                greater.append(v)

    return  quicksort(less)+[pivot]+quicksort(greater)



print(quicksort([10,4,16,20,30,8]))


