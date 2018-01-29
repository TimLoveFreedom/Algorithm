__author__ = 'jellyzhang'
from linkedlist.LinkedList import *

'''
Input: (2 -> 4 -> 3) + (5 -> 6 -> 4)
Output: 7 -> 0 -> 8
Explanation: 342 + 465 = 807.
'''
LinkedListA=SingleLinkedList()
LinkedListA.append(2)
LinkedListA.append(4)
LinkedListA.append(3)
LinkedListB=SingleLinkedList()
LinkedListB.append(5)
LinkedListB.append(6)
LinkedListB.append(4)


LinkedListResult=SingleLinkedList()
currentA=LinkedListA._head
currentB=LinkedListB._head
tmpTag=0
while currentA!=None and currentB!=None:
    resultValue=(currentA.value+currentB.value+tmpTag)%10
    tmpTag=(currentA.value+currentB.value)//10
    LinkedListResult.append(resultValue)
    currentA=currentA.getNext()
    currentB= currentB.getNext()


#多余的节点补上
if currentA==None and currentB==None:
    if tmpTag!=0:
        LinkedListResult.append(tmpTag)
else:
    current=currentA if currentB==None else currentB
    LinkedListResult.append(current.value+tmpTag)
    while current.getNext()!=None:
        LinkedListResult.append(current.getNext().value)
        current=current.getNext()



######print###################
head=LinkedListResult._head
while head!=None:
    print(head.value)
    head=head.getNext()

