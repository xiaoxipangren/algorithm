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
                    items[j+step] = temp
                j = j+step
        if step==1:
            break
    return items




        

def switch(items,src,dest):
    temp = items[src]
    items[src]=items[dest]
    items[dest]=temp


def test(sortm):
    items = numpy.random.randint(0,100,20)
    print(items)
    print(sort(items,sortm))
    print()

if __name__ =='__main__':
    test(shell)

