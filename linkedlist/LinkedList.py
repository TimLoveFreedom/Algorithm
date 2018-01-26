__author__ = 'jellyzhang'
'''
define the Node
'''
class Node(object):
    __slots__ = ['value', 'next']
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
        if self.isEmpty():
            self._head=tmp
        else:
            currentNode=self._head
            while currentNode.getNext()!=None:
                currentNode=currentNode.getNext()
            currentNode.setNext(tmp)
    #search检索元素是否在链表中
    def search(self,item):
        current=self._head
        isExist=False
        while current!=None and not isExist:
            if current.value==item:
                isExist=True
            else:
                current=current.getNext()
        return  isExist
    #index索引元素在链表中的位置(存在则返回大于0的正数，不存在返回0)
    def index(self,item):
        count=0
        current = self._head
        isExist = False
        while current != None and not isExist:
            count+=1
            if current.value == item:
                isExist = True
            else:
                current = current.getNext()
        if isExist:
            return count
        else:
            return 0
    #remove删除链表中的某项元素
    def remove(self,item):
        current=self._head
        pre=None
        while current!=None :
            if current.getData()==item:
                if not pre:
                    self._head=current.getNext()
                else:
                    pre.setNext(current.getNext())
                break
            else:
                pre=current
                current=current.getNext()
    #insert在链表的指定位置添加节点
    def insert(self,position,item):
        if position<0 or position>self._size:
            raise('position error')
        tmp=Node(item)
        if self._size==position:
            self.append(tmp)
        else:
            count=1
            pre=None
            current=self._head
            while count<=position and current!=None:
                if count==position:
                    pre=current.getNext()
                    current.setNext(tmp)
                    tmp.setNext(pre)
                else:
                    current=current.getNext()
                    count+=1
            self._size+=1











