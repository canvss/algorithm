# -*- coding: utf-8 -*-
# @Date     :2022/3/7 19:31
# @Author   :Stephen•Liu
# @FileName :01-hanoi.py
# @Email    :endliss@sina.cn

'''
汉诺塔
'''

def hanoi(n,a,b,c):
    if n > 0:
        hanoi(n-1,a,c,b)
        print(('moving %s from %s'),(a,c))
        hanoi(n-1,b,a,c)

hanoi(3,'A','B','C')