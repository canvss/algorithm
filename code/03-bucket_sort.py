# _*_ coding: utf-8 _*_
# created by Stephen•Liu on 2022/3/14 20:03
'''
    桶排序
'''
import copy
import random
from cal_time import *

@cal_time
def bucket_sort(li ,n=100 ,max_num=10000):
    buckets=[[] for _ in range(n)]  #创建桶
    for var in li:
        i = min(var//(max_num//n),n-1)
        buckets[i].append(var) #往对应的桶添加数据
        # 保持桶里的顺序
        for j in range(len(buckets[i])-1 ,0 ,-1):
            if buckets[i][j] < buckets[i][j-1]:
                buckets[i][j-1],buckets[i][j] = buckets[i][j],buckets[i][j-1]

            else:
                break
    sort_li = []
    # 将所有桶放到sort_li 列表
    for buc in buckets:
        sort_li.extend(buc) #将这个列表数据添加到sort_li列表中
    return sort_li

@cal_time
def count_sort(li,max_count=1000):
    count = [0 for _ in range(max_count+1)]
    for val in li:
        count[val] += 1
    li.clear()
    for i ,val in enumerate (count):
        for j in range(val):
            li.append(i)


li = [random.randint(0,1000) for _ in range(10000)]
li1 = copy.deepcopy(li)
li2 = copy.deepcopy(li)
bucket_sort(li1)
count_sort(li2)