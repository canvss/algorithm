# -*- coding: utf-8 -*-
# @Date     :2022/3/7 21:01
# @Author   :Stephen•Liu
# @FileName :02-linear_search.py
# @Email    :endliss@sina.cn

'''
    顺序查找
'''

def linear_search(li,val):
    for i,v in enumerate(li):
        if v == val:
            return i
    else:
         return None

li = [1,2,5,6,4,9,12,3]
index = linear_search(li,9)