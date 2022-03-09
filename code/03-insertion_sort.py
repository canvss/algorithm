# -*- coding: utf-8 -*-
# @Date     :2022/3/8 21:04
# @Author   :Stephen•Liu
# @FileName :03-insertion_sort.py
# @Email    :endliss@sina.cn

'''
    插入排序法
'''

def insert_sort(li):
    for i in range(1,len(li)):  #发到手上的牌
        tmp = li[i] #摸到的牌
        j = i - 1   #手上的牌
        while j >= 0 and li[j] > tmp:
            li[j+1] = li[j]     #移位
            j -= 1
        li[j+1] = tmp

li = [5,3,7,4,9,2,1,8]
insert_sort(li)
print(li)