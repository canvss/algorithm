# _*_ coding: utf-8 _*_
# created by Stephen•Liu on 2022/4/12 21:32
from functools import cmp_to_key

li = [32, 94, 128, 1286, 6, 71]


def xy_cap(x, y):
    if x + y < y + x:
        return 1
    elif x + y > y + x:
        return -1
    else:
        return 0


def number_join(li):
    """
    :param li:
    :return: str
    """
    li = list(map(str, li))
    li.sort(key=cmp_to_key(xy_cap))
    return "".join(li)


print(number_join(li))

