# -*- coding: utf-8 -*-
# @Date     :2022/3/7 19:27
# @Author   :Stephen•Liu
# @FileName :01-recursion.py
# @Email    :endliss@sina.cn

def recursion(i):
    if i > 0:
        print(i)
        recursion(i-1)


def recursion2(i):
    if i > 0:
        recursion2(i-1)
        print(i)

# recursion(3)
recursion2(3)