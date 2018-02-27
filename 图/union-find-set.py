__author__ = 'jellyzhang'
'''
并查集
'''
class UnionFindSet(object):
    def __init__(self):
        self.root={}

    def find(self,u):
        if u not in self.root:
            self.root[u]=u
            return self.root[u]
        else:
            while u!=self.root[u]:
                u=self.root[u]
            return u

    def union(self,u,v):
        u_root=self.find(u)
        v_root=self.find(v)
        if u_root!=v_root:
            self.root[u_root]=v_root


if __name__=='__main__':
    ufs=UnionFindSet()
    ufs.union('A','B')
    ufs.union('B', 'C')
    ufs.union('B', 'D')
    ufs.union('E', 'F')
    ufs.union('F', 'G')
    print(ufs.root)
    route=set()
    for word in ufs.root.keys():
        route.add(ufs.find(word))
    print('图连通分量：{}'.format(len(route)))