# _*_ coding: utf-8 _*_
# created by Stephen•Liu on 2022/4/13 22:46

from cal_time import cal_time

p = [0, 1, 5, 8, 9, 10, 17, 17, 20, 21, 23, 24, 26, 27, 27, 28, 30, 33, 36, 39, 40]


def cut_rod_rec(p, n):
    res = p[n]
    for i in range(1, n):
        res = max(res, cut_rod_rec(p, i) + cut_rod_rec(p, n - i))
    return res


@cal_time
def cut1(p, n):
    return cut_rod_rec(p, n)


def cut_rod_rec_2(p, n):
    res = p[n]
    for i in range(1, n):
        res = max(res, p[i] + cut_rod_rec_2(p, n - i))
    return res


@cal_time
def cut2(p, n):
    return cut_rod_rec_2(p, n)


def cut_rod_dp(p ,n):
    r = [0]
    for i in range(1, n+1):
        res = 0
        for j in range(1, i+1):
            res = max(res, r[i-j]+p[j])
        r.append(res)
    return r[n]


print(cut_rod_dp(p, 20))
