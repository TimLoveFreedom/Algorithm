__author__ = 'jellyzhang'
'''
tree 广度遍历
'''
import  queue
class Node(object):
    def __init__(self,data=None,left=None,right=None):
        self.data=data
        self.left=left
        self.right=right

#init
root=Node('A')
left_layer1=Node('B')
right_layer1=Node('C')
root.left=left_layer1
root.right=right_layer1

left_layer21=Node('D')
right_layer22=Node('E')
left_layer23=Node('F')
right_layer24=Node('G')

left_layer1.left=left_layer21
left_layer1.right=right_layer22
right_layer1.left=left_layer23
right_layer1.right=right_layer24



queue=queue.Queue()
queue.put(root)
while(not queue.empty()):
    node=queue.get()
    print(node.data)
    if node.left!=None:
        queue.put(node.left)
    if node.right!=None:
        queue.put(node.right)