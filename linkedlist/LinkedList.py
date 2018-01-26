__author__ = 'jellyzhang'
'''
define the Node
'''
class Node(object):
    def __init__(self,val,next=None):
        self.value=val
        self.next=next
    def getData(self):
        return self.value
    def setData(self,newData):
        self.value=newData
    def getNext(self):
        return  self.next
    def setNext(self,newNext):
        self.next=newNext


'''
define the linkedlist
'''
class SingleLinkedList(object):
    def __init__(self):
        self._head=None
        self._size=0
    #检测链表是否为空
    def isEmpty(self):
        return  self._head==None
    #add在链表前端添加元素
    def add(self,item):
        tmp=Node(item)
        tmp.setNext(self._head)
        self._head=tmp
    #append在链表尾部添加元素
    def append(self,item):
        tmp=Node(item)
        if self._size==0:
            self._head




