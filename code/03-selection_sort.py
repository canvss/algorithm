# -*- coding: utf-8 -*-
# @Date     :2022/3/8 19:45
# @Author   :Stephen•Liu
# @FileName :03-selection_sort.py
# @Email    :endliss@sina.cn
'''
    选择排序
'''

def select_sort(li):
    for i in range(len(li)-1):    #第i趟
        min_loc = i
        for j in range(i+1,len(li)):
            if li[j] < li[min_loc]:
                min_loc = j     #将最小值赋值给min_loc
        li[min_loc] , li[i] = li[i] , li[min_loc]   #待排序区域最小值放到元素开始下标

li = [5,7,2,6,9,1,4,8,3]
select_sort(li)
print(li)
