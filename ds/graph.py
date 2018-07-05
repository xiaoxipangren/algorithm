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
        if matrix[head][tail]==0:
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
        if matrix[head][tail]==0:
            return self.taillink(head+1,tail,map)
        
        node = None
        if (head,tail) not in map:
            node = LinkNode(head,tail)
            map[(head,tail)]=node
        else:
            node=map[(head,tail)]
        node.taillink=self.taillink(head+1,tail,map)
        return node

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
    data=['v0','v1','v2','v3']
    matrix = [
        [0,0,0,1],
        [1,0,1,0],
        [1,1,0,0],
        [0,0,0,0]
    ]
    graph = Graph(data,matrix)

    nodes = graph.toLink()

    for node in nodes:
        node.println()
