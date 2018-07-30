class BinNode:
    def __init__(self,data,left=None,right=None):
        self.data=data
        self.left=left
        self.right=right

def build(array):
    data = array.pop(0)
    if data == '#':
        return None
    node = BinNode(data)
    node.left = build(array)
    node.right = build(array)
    return node


def left_max(node):
    while node.right != None:
        node = node.right
    return node    
    

def leaf(node):
    return node.left == None and node.right == None

def child(node):
    return (node.left == None) != (node.right == None)
def children(node):
    return node.left != None and node.right != None

def insert(data,tree):
    if tree == None:
        return
    node = find(data,tree)
    if node.data == data:
        return 
    new = BinNode(data)

    if data > node.data:
        node.right = new
    if data < node.data:
        node.left = new

def findParent(tree,node):
    if tree == None:
        return None
    if tree.left!= None and tree.left.data==node.data:
        return tree
    if tree.right != None and tree.right.data == node.data:
        return tree
    if tree.data > node.data:
        return findParent(tree.left,node)
    if tree.data < node.data:
        return findParent(tree.right,node)


def find(data,node):
    if node == None:
        return None

    if node.data == data:
        return node
    if node.data>data:
        if node.left == None:
            return node
        return find(data,node.left)
    if node.data<data:
        if node.right == None:
            return node
        return find(data,node.right)

def remove(data,tree):
    node = find(data,tree)

    if node == tree:#root node
        if tree.left == None:
            return tree.left
        else:
            max = left_max(tree.left)
            max.right = tree.right
            tree.right = None
            return max
    else:
        parent = findParent(tree,node)
        if leaf(node):
            if parent.left == node:
                parent.left = None
            else:
                parent.right = None
        elif child(node):
            kid = node.left if node.left!= None else node.right
            if parent.left == node:
                parent.left = kid
            else:
                parent.right = kid
            node.left = None
            node.right = None
        elif children(node):
            max = left_max(node.right)
            max.right = node.left
            if parent.left == node:
                parent.left = max
            else:
                parent.right = max
            node.left = None
            node.right = None
        return tree


def mid(node):
    list =[]
    mid_visit(node,list)
    return list

def mid_visit(node,list):
    if node == None:
        return
    mid_visit(node.left,list)
    list.append(node.data)
    mid_visit(node.right,list)

def bin(item,items):
    start = 0
    end = len(items)

    mid = (start+end)//2
    while mid >=0 and mid <len(items):
        if item>items[mid]:
            start = mid+1#注意+1
        elif item<items[mid]:
            end = mid -1#注意-1
        else:
            return mid
        mid = (start+end)//2
    return -1


if __name__ == '__main__':
    items=[7,3,1,'#','#',5,'#','#',11,9,'#','#',13,'#','#']
    tree = build(items)


    