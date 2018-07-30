import random

class Graph:
    def __init__(self,data,matrix):
        self.data=data
        self.matrix=matrix
    
    def println(self):
        print(self.data)
        print(self.matrix)
    
    def toLink(self):
        nodes=[]
        map={}
        for i in range(len(self.data)):
            node = DataNode(self.data[i])
            node.inlink = self.taillink(0,i,map)
            node.outlink = self.headlink(i,0,map)
            nodes.append(node)
        return nodes
    
    def headlink(self,head,tail,map):
        if tail>=len(self.data):
            return None
        if self.matrix[head][tail]==0:
            return self.headlink(head,tail+1,map)
        node = None
        if (head,tail) not in map:
            node = LinkNode(head,tail)
            map[(head,tail)]=node
        else:
            node = map[(head,tail)]
        node.headlink=self.headlink(head,tail+1,map)

        return node

    def taillink(self,head,tail,map):
        if head>=len(self.data):
            return None
        if self.matrix[head][tail]==0:
            return self.taillink(head+1,tail,map)
        
        node = None
        if (head,tail) not in map:
            node = LinkNode(head,tail)
            map[(head,tail)]=node
        else:
            node=map[(head,tail)]
        node.taillink=self.taillink(head+1,tail,map)
        return node
    #深度优先遍历，先序遍历
    def dfs(self):
        mark=[]
        index = random.randint(0,len(self.data)-1)
        self.deep(index,mark)
        return [self.data[i] for i in mark]
    
    #广度优先遍历，层序遍历
    def bfs(self):
        mark=[]
        index = random.randint(0,len(self.data)-1)

        nodes = [index]
        while len(nodes)>0:
            index = nodes.pop(0)
            mark.append(index)
            for i in range(len(self.data)):
                if self.matrix[index][i]>0 and i not in mark and i not in nodes:
                    nodes.append(i)
        return [self.data[i] for i in mark]


    def mintree(self):
        left = []
        index = random.randint(0,len(self.data)-1)
        low = [float('inf')]*len(self.data)
        vex=[0]*len(self.data)
        left.append(index)
        sides=[]
        while len(left) < len(self.data):
            index = left[-1]
            for i in range(len(self.data)):
                if self.matrix[index][i] > 0 and self.matrix[index][i]<low[i]:
                    low[i]=self.matrix[index][i]
                    vex[i]=index

            min=float('inf')
            j=0
            for i in range(len(low)):
                if low[i] < min and i not in left:
                    min = low[i]
                    j=i
            sides.append((vex[j],j))
            left.append(j)
        
        return sides
            



    #贪心法，最短路径上的节点都是其最短路径   
    def short(self,start,end):
        vex = []
        length = len(self.data)
        path = [start]*length
        
        for i in range(length):
            for j in range(length):
                if self.matrix[i][j] == 0:
                    self.matrix[i][j] = float('inf')

        low =[float('inf')]*length

        vex.append(start)
        for i in range(length):
                low[i] = self.matrix[start][i]

        while len(vex) < length:    
            min = float('inf')
            j=0
            for i in range(length):
                if low[i] < min and i not in vex:
                    min = low[i]
                    j=i
            vex.append(j)

            for i in range(length):
                if i not in vex and low[j] + self.matrix[j][i] < low[i]:
                    low[i] = low[j] + self.matrix[j][i]
                    path[i] = j #注意记录最短路径的节点链，一次扫描可获得所有其他节点的最短路径
        
        link = []
        i = end 
        while True:
            link.insert(0,i)
            if i == start:
                break
            i = path[i]
        return (link,path)


    def deep(self,index,mark):
        if index in mark:
            return
        mark.append(index)

        for i in range(len(self.data)):
            if self.matrix[index][i]>0:
                self.deep(i,mark)

        


class DataNode:
    def __init__(self,data,inlink=None,outlink=None):
        self.data=data
        self.inlink=inlink
        self.outlink=outlink
    
    def println(self):
        print(self.data)
        print("outlink")
        
        node = self.outlink
        while node!=None:
            node.println()
            node = node.headlink

        print("inlink")
        node = self.inlink
        while node!=None:
            node.println()
            node = node.taillink
        print()

class LinkNode:
    def __init__(self,head,tail,headlink=None,taillink=None):
        self.tail=tail
        self.taillink=taillink
        self.head=head
        self.headlink=headlink

    def println(self):
        print(self.head,self.tail)


        

if __name__=='__main__':
    data=['A','B','C','D','E','F','G','H','I']
    #最短路径测试用例
    matrix_short = [
        [0,1,5,0,0,0,0,0,0],
        [1,0,3,7,5,0,0,0,0],
        [5,3,0,0,1,7,0,0,0],
        [0,7,0,0,2,0,3,0,0],
        [0,5,1,2,0,3,6,9,0],
        [0,0,7,0,3,0,0,5,0],    
        [0,0,0,3,6,0,0,2,7],
        [0,0,0,0,9,5,2,0,4],
        [0,0,0,0,0,0,7,4,0]
    ]



    graph = Graph(data,matrix_short)

    nodes = graph.dfs()

    print(nodes)

    nodes = graph.bfs()

    print(nodes)

    nodes = graph.short(1,8)
    print(nodes)
