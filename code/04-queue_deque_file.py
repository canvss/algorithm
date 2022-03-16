# _*_ coding: utf-8 _*_
# created by Stephen•Liu on 2022/3/16 23:33
'''
    使用python内置队列实现文件后n行的数据
'''

from collections import deque


def tail(n):
    with open('tail.txt', 'r') as f:
        q = deque(f,n)
        return q


for line in tail(4):
    print(line,end='')