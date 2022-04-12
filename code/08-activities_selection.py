# _*_ coding: utf-8 _*_
# created by Stephen•Liu on 2022/4/12 21:51

activities = [(1, 4), (3, 5), (0, 6), (5, 7), (3, 9), (5, 9), (6, 10), (8, 11), (8, 12), (2, 14), (12, 16)]
activities.sort(key=lambda x: x[1])  # 以结束时间排序


def activities_seletion(a):
    """
    :param a:
    :return: res
    """
    res = [a[0]]
    for i in range(1, len(a)):
        if res[-1][1] < a[i][0]:
            res.append(a[i])
    return res


print(activities_seletion(activities))
