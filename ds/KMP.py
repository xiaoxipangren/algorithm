#! encoding=utf-8

import sys


#kmp算法的核心在于模式串的自我匹配，即利用前后缀来避免
#主串指针的回溯，

# 得到next数组的方式实际上是利用对称的方式来的，
# 不断利用并查集得到最长的前后缀

def next(array):
    if array == None:
        return None
    if len(array) == 1:
        return [-1]
    if len(array) == 2:
        return [-1,0]
    next=[1] * len(array)
    next[0]=-1
    next[1]=0
    i=2
    j=0
    while i<len(array):
        if j==-1 or array[i-1]==array[j]:
            j=j+1
            next[i]=j
            i=i+1
        else:
            j=next[j]
    return next

def find(string,pattern):
    array = next(pattern)
    print(array)
    i=0
    j=0
    while i<len(string) and j<len(pattern):
        if string[i]==pattern[j] or j==-1:
            i=i+1
            j=j+1
        else:
            j=array[j]
            
    if j==len(pattern):
        return i-j
    return -1


print(find(sys.argv[1],sys.argv[2]))