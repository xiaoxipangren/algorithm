import numpy

def sort(items,sortm):
    return sortm(items)

def bubble(items):
    for i in range(len(items)-1):
        for j in range(len(items)-i-1):
            if items[j] > items[j+1]:
                switch(items,j+1,j)
    return items

def select(items):
    for i in range(len(items)-1):
        k = i
        for j in range(i+1,len(items)):
            if items[j] < items[k]:
                k = j
        if k!=i:
            switch(items,i,k)
    return items

def insert(items):
    for i in range(len(items)-1):
        if items[i]>items[i+1]:
            temp = items[i+1]
            j = i
            while j>=0 and items[j] > temp:
                items[j+1] = items[j]
                j = j-1
            items[j+1] = temp
    return items

def shell(items):
    step = len(items)
    while True:
        step = step//3+1
        for i in range(step):
            j = i
            while j<len(items)-step:
                if items[j] > items[j+step]:
                    temp = items[j+step]
                    k = j
                    while k>=0 and items[k]>temp:
                        items[k+step] = items[k]
                        k = k -step
                    items[k+step] = temp
                j = j+step
        if step==1:
            break
    return items

def heap(items):
    for i in range(len(items)-1):
        adjust(items,len(items)-i)
        switch(items,0,len(items)-i-1)
    return items

def merge(items):
    step = 1
    while step < len(items):
        mix(items,step)
        step = step * 2
    return items



def mix(items,step):
    i = 0 
    while i < len(items) - step:
        fuse(items,i,step)
        i = i + 2 * step
    print(items)


def fuse(items,start,step):
    temp = []
    left = start
    right = left+step

    while left < start+step and left < len(items) and right<len(items) and right < start+2*step:
        if items[left] <= items[right]:
            temp.append(items[left])
            left = left+1
        else:
            temp.append(items[right])
            right = right +1
    
    while left < start + step and left < len(items):
        temp.append(items[left])
        left = left+1
          
    while right < start + 2*step and right < len(items):
        temp.append(items[right])
        right = right+1
    
    for i in range(len(temp)):
        items[start+i] = temp[i]
    

def adjust(items,end):#构建
    node = end//2 -1
    while node >= 0:
        child = bigger(items,node,end)
        if items[node]<items[child]:
            switch(items,node,child)
        node = node -1 


def bigger(items,index,end):
    left = index*2+1
    right = index*2+2

    if right < end:
        return left if items[left]>items[right] else right
    else:
        return left

def switch(items,src,dest):
    temp = items[src]
    items[src]=items[dest]
    items[dest]=temp


def test(sortm):
    items = numpy.random.randint(0,1000,50)
    print(items)
    print(sort(items,sortm))
    print()

if __name__ =='__main__':
    test(merge)

