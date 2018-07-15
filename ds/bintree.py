class BinNode:
    def __init__(self,data,left=None,right=None):
        self.data=data
        self.left=left
        self.right=right

#只有前序遍历的虚拟结点集合才能还原二叉树
def build(array):
    data = array.pop(0)
    if data == '#':
        return None
    node = BinNode(data)
    node.left = build(array)
    node.right = build(array)
    return node

def from_fam(front,mid):
    if len(front) ==0 or len(mid) == 0:
        return None
    if len(front) == 1 or len(mid) ==1:
        return BinNode(front[0])
    
    data = front.pop(0)
    node = BinNode(data)

    left_mid = mid[:mid.index(data)]
    right_mid = mid[mid.index(data)+1:]

    index = 0
    while index<len(front) and front[index] in left_mid:
        index=index+1
    
    left_front = front[:index]
    right_front = front[index:]

    node.left=from_fam(left_front,left_mid)
    node.right = from_fam(right_front,right_mid)

    return node



def from_bam(back,mid):
    if len(back) ==0 or len(mid) == 0:
        return None
    if len(back) == 1 or len(mid) ==1:
        return BinNode(back[0])

    data = back.pop()
    node = BinNode(data)

    left_mid = mid[:mid.index(data)]
    right_mid = mid[mid.index(data)+1:]

    index = 0
    while index<len(back) and back[index] in left_mid:
        index=index+1
    
    left_back = back[:index]
    right_back = back[index:]

    node.left = from_bam(left_back,left_mid)
    node.right= from_bam(right_back,right_mid)

    return node


def visit(node,order):
    list = []
    if order == 'front':
        front_visit(node,list)
    elif order == 'mid':
        mid_visit(node,list)
    elif order == 'back':
        back_visit(node,list)
    else:
        list.append(node)
        list = floor_visit(list)
    return list

def front_visit(node,list):
    if node == None:
        list.append('#')
        return
    list.append(node.data)
    front_visit(node.left,list)
    front_visit(node.right,list)

def mid_visit(node,list):
    if node == None:
        list.append('#')
        return
    mid_visit(node.left,list)
    list.append(node.data)
    mid_visit(node.right,list)

def back_visit(node,list):
    if node==None:
        list.append('#')
        return
    back_visit(node.left,list)
    back_visit(node.right,list)
    list.append(node.data)
def floor_visit(list):
    result = []
    while len(list) > 0:
        node = list.pop(0)
        result.append(node.data)
        if node.left!=None:
            list.append(node.left)
        if node.right!=None:
            list.append(node.right)
    return result

if __name__=='__main__':
    # array=['A','B','D','#','F','#','#','#','C','E','#','G','H','#','#','#','#']
    # node = build(array)
    # print(visit(node,'front'))
    # print(visit(node,'mid'))
    # print(visit(node,'back'))
    # print(visit(node,'floor'))

    print(visit(from_bam(list('FDBHGECA'),list('DFBAEHGC')),'back'))