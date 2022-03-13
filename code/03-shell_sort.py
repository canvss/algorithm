# _*_ coding: utf-8 _*_
# created by Stephen•Liu on 2022/3/13 16:58

'''
    希尔排序
'''
import random
from cal_time import *

def insertion_sort_gap(li ,gap):
    for i in range(gap,len(li)):
        tmp = li[i]
        j = i - gap
        while j >= 0 and li[j] > tmp:
            li[j+gap] = li[j]
            j -= gap
        li[j+gap] = tmp

@cal_time
def shell_sort(li):
    d =len(li) // 2
    while d >= 1:
        insertion_sort_gap(li,d)
        d //= 2

li = list(range(16))
random.shuffle(li)
print(li)
shell_sort(li)
print(li)
