# _*_ coding: utf-8 _*_
# created by Stephen•Liu on 2022/3/11 22:46
'''
    使用python堆的内置模块
'''

import heapq
import random

li = list(range(100))
random.shuffle(li)

print(li)

# 构建堆
heapq.heapify(li)

n = len(li)

for i in range(n):
    print(heapq.heappop(li),end=',')
