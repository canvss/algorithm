# _*_ coding: utf-8 _*_
# created by Stephen•Liu on 2022/4/14 22:24

def lcs_length(x, y):
    m = len(x)
    n = len(y)
    c = [[0 for _ in range(n+1)] for _ in range(m+1)]
    for i in range(1, m+1):
        for j in range(1, n+1):
            if x[i-1] == y[j-1]:
                c[i][j] = c[i-1][j-1]+1
            else:
                c[i][j] = max(c[i-1][j],c[i][j-1])

    for _ in c:
        print(_)

    return c[m][n]


def lcs(x, y):
    m = len(x)
    n = len(y)
    c = [[0 for _ in range(n + 1)] for _ in range(m + 1)]
    b = [[0 for _ in range(n + 1)] for _ in range(m + 1)]  # 左上方  上方  左方
    for i in range(1, m + 1):
        for j in range(1, n + 1):
            if x[i - 1] == y[j - 1]:  # i,j位置上的字符匹配的时候，来自于左上方+1
                c[i][j] = c[i - 1][j - 1] + 1
                b[i][j] = 1
            elif c[i - 1][j] >= c[i][j - 1]:  # 来自于上方(这里把等于也偏向上)
                c[i][j] = c[i - 1][j]
                b[i][j] = 2
            else:  # 来自于左方
                c[i][j] = c[i][j - 1]
                b[i][j] = 3
    return c[m][n], b


c, b = lcs("ABCBDAB", "BDCABA")

for _ in b:
    print(_)


def lcs_trackback(x,y):
    c, b = lcs(x, y)
    i = len(x)
    j = len(y)
    res = []
    while i > 0 and j > 0:
        if b[i][j] == 1:   # 来自左上方 -- 匹配
            res.append(x[i-1])
            i -= 1
            j -= 1
        elif b[i][j] == 2:   # 来自于上方 -- 不匹配
            i -= 1
        else:       # ==3,来自左方 -- 不匹配
            j -= 1
    print(res)
    return "".join(reversed(res))


