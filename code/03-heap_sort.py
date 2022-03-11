# _*_ coding: utf-8 _*_
# created by Stephen•Liu on 2022/3/11 20:19
import random


# 堆调整
def sift(li,low,high):
    """
    :param li: 列表
    :param low: 堆的根节点位置
    :param high: 堆最后一个元素的位置
    :return:
    """
    i = low #i最开始指向根节点
    j = 2 * i + 1   #j是左孩子
    tmp = li[low]     #将堆顶的值存起来
    while j <= high:    #j的值不能超过堆的最后一个元素
        if j + 1 <= high and li[j+1] > li[j]: #如果有右孩子并且比左孩子大，就把j指向右孩子
            j += 1
        if li[j] > tmp: #如果孩子大于堆顶，就交换他们的位置
            li[i] = li[j]
            i = j       #将i指向新的堆顶，向下看一层
            j = 2 * i +1    #根据堆顶求出左孩子
        else:
            break
    li[i] = tmp #如果j超过了high，或者孩子小于堆顶，就把tmp放回原位置


# 堆排序
def heap_sort(li):
    n = len(li)
    # 构建堆
    for i in range((n-2)//2,-1,-1): #i表示建堆时部分根下标
        sift(li,i,n-1)  #将堆的最后一个元素作为high
    print(li)
    for i in range(n-1 ,-1 ,-1):    #i指当前堆的最后一个元素
        li[i] ,li[0] = li[0] ,li[i] #把当前堆顶和堆的最后一个元素交换位置
        sift(li ,0 ,i - 1)


li = [i for i in range(100)]
random.shuffle(li)
heap_sort(li)
print(li)


