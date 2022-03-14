# _*_ coding: utf-8 _*_
# created by Stephen•Liu on 2022/3/14 21:16
'''
    基数排序
'''
import copy
import random
from cal_time import *

@cal_time
def radix_sort(li):
    max_num = max(li)
    it =0
    # 10的it次方
    while 10 ** it <= max_num:
        buckets = [[] for _ in range(10)]
        # 1、把对应的数据放到对应的桶
        for var in li:
            # max_num = 974；取十位，it=1，974//10 --> 97 % 10 -->7
            digit = (var//10 ** it) % 10
            buckets[digit].append(var)

        # 2、将原来的li列表清空
        li.clear()
        # 3、将新的列表放回li列表
        for buc in buckets:
            li.extend(buc)
        it += 1

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


li = [random.randint(0,1000000000) for _ in range(1000)]
li1 = copy.deepcopy(li)
li2 = copy.deepcopy(li)
bucket_sort(li1)
radix_sort(li2)