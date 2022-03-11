# _*_ coding: utf-8 _*_
# created by Stephen•Liu on 2022/3/11 22:11
import random

def sift(li,low,high):
    i = low
    j = 2 * i +1
    tmp = li[i]
    while j <= high:
        if j+1 <= high and li[j+1] < li[j]:
            j +=1
        if li[j] < tmp:
            li[i] = li[j]
            i = j
            j = 2*i+1
        else:
            break
    li[i] = tmp

def heap_topk(li,k):
    heap = li[0:k]
    for i in range((k-2)//2 ,-1 ,-1):
        sift(heap ,i ,k-1)

    # 1、构建堆
    for i in range(k ,len(li)-1):
        if li[i] > heap[0]:
            heap[0] = li[i]
            sift(heap,0,k-1)

    #2、遍历
    for i in range(k-1 ,-1 ,-1):
        heap[0] ,heap[i] = heap[i] ,heap[0]
        sift(heap ,0 ,i-1)

    # 出数
    return heap

li = list(range(1000))
random.shuffle(li)
heap = heap_topk(li,10)
print(heap)
