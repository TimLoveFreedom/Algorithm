__author__ = 'jellyzhang'
'''
graph bfs
'''
import queue

q=queue.Queue()
graph = {'A': ['B', 'C', 'E'],
         'B': ['A','D', 'E'],
         'C': ['A', 'F', 'G'],
         'D': ['B'],
         'E': ['A', 'B','D'],
         'F': ['C'],
         'G': ['C']}

def bfs(graph,start):
    visited=[]
    q.put(start)
    while not q.empty():
        element=q.get()
        if element in visited: #访问过
            continue
        else: #没有访问过
            visited.append(element)
            print(element)
            for e in graph[element]:
                q.put(e)


bfs(graph,'A')
