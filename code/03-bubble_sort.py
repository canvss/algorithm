# -*- coding: utf-8 -*-
# @Date     :2022/3/8 13:19
# @Author   :Stephen•Liu
# @FileName :03-bubble_sort.py
# @Email    :endliss@sina.cn

'''
    冒泡排序
'''
import random


def bubble_sort(li):
    for i in range(len(li) - 1):    #第i躺
        exchange = False
        for j in range(len(li) - i -1):
            if li[j] > li[j+1]:
                li[j],li[j+1] = li[j+1],li[j]   #交换位置
                exchange = True
        if not exchange:
            return


li = [random.randint(1,100) for i in range(10)]
print(li)
bubble_sort(li)
print(li)