# _*_ coding: utf-8 _*_
# created by Stephen•Liu on 2022/3/14 13:00

'''
    计数排序
'''
import copy
import random
from cal_time import *

@cal_time
def count_sort(li,max_count=100):
    count = [0 for _ in range(max_count+1)]
    for val in li:
        count[val] += 1
    li.clear()
    for i ,val in enumerate (count):
        for j in range(val):
            li.append(i)

@cal_time
def sys_sort(li):
    li.sort()

li = [random.randint(0,100) for _ in range(1000)]
li1 = copy.deepcopy(li)
li2 = copy.deepcopy(li)
count_sort(li1)
sys_sort(li2)
