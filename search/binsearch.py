__author__ = 'jellyzhang'

'''
折半查找（二分查找）
'''

def BinSearch(arr,key,low,high):
    mid=(low+high)//2
    if low>high:
        return False
    if arr[mid]==key:
        return arr[mid]
    elif arr[mid]>key:
        return BinSearch(arr,key,low,mid-1)
    else:
        return BinSearch(arr,key,mid+1,high)

if __name__ == "__main__":
    a=[1,2,4,10,20,24,30,31,40,50,69,70,80,91]
    ret=BinSearch(a,40,0,len(a)-1)
    print(ret)



