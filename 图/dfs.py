from 栈.stack import Stack

__author__ = 'jellyzhang'
'''
graph dfs
'''
graph = {'A': ['B', 'C', 'E'],
         'B': ['A','D', 'E'],
         'C': ['A', 'F', 'G'],
         'D': ['B'],
         'E': ['A', 'B','D'],
         'F': ['C'],
         'G': ['C']}

def bfs(graph,start):
    visited=[]
    stack=Stack()
    stack.push(start)
    while not stack.isEmpty():
        element=stack.pop()
        if element in visited: #访问过
            continue
        else: #没有访问过
            visited.append(element)
            print(element)
            for e in graph[element]:
                stack.push(e)


bfs(graph,'A')
