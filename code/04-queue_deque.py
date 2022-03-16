# _*_ coding: utf-8 _*_
# created by Stephen•Liu on 2022/3/16 23:42
from collections import deque

q = deque([1,2,3,4,5,6],6)
q.appendleft(-1)
q.append(7)
# print(q.popleft())
# print(q)
# print(q.pop())
# print(q.popleft())
print(q.popleft())
