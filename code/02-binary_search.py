# -*- coding: utf-8 -*-
# @Date     :2022/3/7 21:37
# @Author   :Stephen•Liu
# @FileName :02-binary_search.py
# @Email    :endliss@sina.cn

'''
    二分查找法
'''

def binary_search(li,val):
    left = 0
    right = len(li) - 1
    while right >= left:    #候选区有值
        mid = (left + right) // 2
        if li[mid] == val:
            return mid
        elif li[mid] > val:  #候选区在mid左边
            right = mid - 1
        else:   #li[mid] < val 候选区在mid右边
            left = mid + 1
    else:
        return None

li = [1,2,3,4,5,6,7,8,9,10]
binary_search(li,3)