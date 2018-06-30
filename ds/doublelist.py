class DoubleListNode:
    def __init__(self,data=None):
        self.data=data
        self.pre=None
        self.next=None

def build(list):
    if list==None or len(list)==0:
        return None
    head=DoubleListNode(list[0])
    current=head
    for data in list[1:]:
        node = DoubleListNode(data)
        node.pre=current
        current.next=node
        current=node
    return head
def visit(node):
    while node !=None:
        print(node.data)
        node=node.next

def insert(node,data):
    temp = DoubleListNode(data)
    node.next.pre=temp
    temp.next=node.next
    node.next=temp
    temp.pre=node
    

def length(head):
    length = 0
    while head != None:
        head=head.next
        length=length+1
    return length

def get(index,node):
    for i in range(index):
        if node.next==None:
            return node
        node = node.next

    return node

if __name__=='__main__':
    head = build([1,2,3,4,5])

    node = get(3,head)
    insert(node,7)
    visit(head)
