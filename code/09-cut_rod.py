# _*_ coding: utf-8 _*_
# created by Stephen•Liu on 2022/4/13 22:46

from cal_time import cal_time

p = [0, 1, 5, 8, 9, 10, 17, 17, 20, 21, 23, 24, 26, 27, 27, 28, 30, 33, 36, 39, 40]


def cut_rod_rec(p, n):
    if n == 0:
        return 0
    res = 0
    for i in range(1, n):
        res = max(res, cut_rod_rec(p, i) + cut_rod_rec(p, n - i))
    return res


@cal_time
def cut1(p, n):
    return cut_rod_rec(p, n)


def cut_rod_rec_2(p, n):
    if n == 0:
        return 0
    res = 0
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


def cut_rod_extent(p, n):
    r = [0]     # 最优解
    s = [0]     # 切割后左边的长度
    for i in range(1, n+1):
        res_r = 0
        res_s = 0
        for j in range(1, i+1):
            if p[j] + r[i-j] > res_r:
                res_r = p[j] + r[i-j]
                res_s = j
        r.append(res_r)
        s.append(res_s)
    return r[n], s

def cut_rod_solution(p, n):
    r, s = cut_rod_extent(p, n)
    end = []
    while n > 0:
        end.append(s[n])
        n -= s[n]
    return end



print(cut_rod_solution(p, 9))
