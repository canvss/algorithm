# _*_ coding: utf-8 _*_
# created by Stephen•Liu on 2022/3/13 14:41

'''
    归并排序
'''
import random


def merge(li ,low ,mid ,high):
    i = low
    j = mid+1
    ltmp = []   # 用于临时存放排序好的列表
    # 左右两边都有数
    while i <= mid and j <= high:   # 如果左边部分小于mid并且右边部分小于high
        if li[i] < li[j]:   # 选出左右两边小的值
            ltmp.append(li[i])  # 将左边值添加到新的列表
            i += 1  # 将下标往后移动
        else:
            ltmp.append(li[j])
            j += 1
    # 有可能右边没数，但左边还有数
    while i <= mid:
        ltmp.append(li[i])
        i += 1
    # 有可能左边没数，但右边还有数
    while j <= high:
        ltmp.append(li[j])
        j += 1

    li[low:high+1] = ltmp

def merge_sort(li ,low ,high):
    if low < high:      #至少有两个数
        mid = (low + high)//2
        merge_sort(li,low,mid)
        merge_sort(li,mid+1,high)
        merge(li ,low ,mid ,high)

li = list(range(16))
random.shuffle(li)
print(li)
merge_sort(li ,0 ,len(li)-1)
print(li)