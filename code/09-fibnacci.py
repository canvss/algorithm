# _*_ coding: utf-8 _*_
# created by Stephen•Liu on 2022/4/13 21:23


def fibnacci(n):
    """
    1 1 2 3 5 8 13 21 34......
    :param n:
    :return : val
    """
    if n == 1 or n == 2:
        return 1
    else:
        return fibnacci(n-1) + fibnacci(n-2)


def fibnacci_no_rec(n):
    """
    :param n:
    :return:
    """
    f = [0, 1]
    if n > 2:
        for i in range(n-2):
            num = f[-1]+f[-2]
            f.append(num)
    return f[n]


print(fibnacci_no_rec(20))