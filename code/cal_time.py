# _*_ coding: utf-8 _*_
# created by Stephen•Liu on 2022/3/8 23:15

import time

def cal_time(func):
    def wrapper(*args, **kwargs):
        t1 = time.time()
        result = func(*args, **kwargs)
        t2 = time.time()
        print("%s running time: %s secs." % (func.__name__, t2 - t1))
        return result

    return wrapper