
def compare(left,right):
    mid = 44.2
    left = abs(left-mid)
    right = abs(right-mid)

    return 0 if abs(left-right)<=0.6 else left-right

def toPolish(items):
    result=[]
    stack=[]
    for item in items:
        if item.isdigit():
            result.append(item)
        else:
            if len(stack) == 0 or item == '(':
                stack.append(item)
            elif item == ')':
                top = stack.pop()
                while len(stack)>0 and top!='(':
                    result.append(top)
                    top = stack.pop()
            else:
                while len(stack)>0 and stack[-1]!='(' and compare(ord(stack[-1]),ord(item))>=0:
                    result.append(stack.pop())
                stack.append(item)
    while len(stack)>0:
        result.append(stack.pop())
    return result

def calculate(items):
    stack=[]
    for item in items:
        if item.isdigit():
            stack.append(item)
        else:
            right = int(stack.pop())
            left = int(stack.pop())
            result = 0
            if item =='*':
                result = left*right
            elif item=='/':
                result = left/right
            elif item=='+':
                result = left + right
            elif item =='-':
                result = left -right
            stack.append(result)
    
    return stack.pop()
            


if __name__=='__main__':
    items=['5','+','6','*','(','3','+','4',')','-','2','*','3']
    items=toPolish(items)
    print(calculate(items))
                