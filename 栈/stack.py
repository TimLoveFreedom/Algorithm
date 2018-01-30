__author__ = 'jellyzhang'

class Stack(object):
    def __init__(self):
        self.__items=[]
    def isEmpty(self):
        return len(self.__items)==0
    def push(self,item):
        return self.__items.append(item)
    def pop(self):
        return self.__items.pop()
    def peek(self):
        if not self.isEmpty():
            return self.__items[len(self.__items)-1]
    def size(self):
        return self.__items


