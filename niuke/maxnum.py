
def maxNum(array):

    i=0
    while i < len(array)-1:
        k=i
        j=i+1
        while j < len(array):
            if bigger(array[j],array[k]):
                k=j
            j=j+1
        if k!=i:
            str=array[k]
            array[k]=array[i]
            array[i]=str
        i=i+1                                                 
    return ''.join(array)


def bigger(left,right):
    if left==right:
        return False
    if left.startswith(right) or right.startswith(left):
       return (left+right)>(right+left)
    
    return left>right


result =[]

while True:
    try:
        str = input()
        str = input()
        result.append(maxNum(str.split(' ')))
    except:
        break

for s in result:
    print(s)
