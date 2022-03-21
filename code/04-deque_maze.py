# _*_ coding: utf-8 _*_
# created by Stephen•Liu on 2022/3/21 20:32
'''
    队列实现走迷宫
'''

from collections import deque


maze = [
    [1, 1, 1, 1, 1, 1, 1, 1, 1, 1],
    [1, 0, 0, 1, 0, 0, 0, 1, 0, 1],
    [1, 0, 0, 1, 0, 0, 0, 1, 0, 1],
    [1, 0, 0, 0, 0, 1, 1, 0, 0, 1],
    [1, 0, 1, 1, 1, 0, 0, 0, 0, 1],
    [1, 0, 0, 0, 1, 0, 0, 0, 0, 1],
    [1, 0, 1, 0, 0, 0, 1, 0, 0, 1],
    [1, 0, 1, 1, 1, 0, 1, 1, 0, 1],
    [1, 1, 0, 0, 0, 0, 0, 0, 0, 1],
    [1, 1, 1, 1, 1, 1, 1, 1, 1, 1]
]
dirs = [
    lambda x,y: (x+1,y),    # 向上走
    lambda x,y: (x-1,y),    # 向下走
    lambda x,y: (x,y-1),    # 向左走
    lambda x,y: (x,y+1)     # 向右走
]

def print_r(path):
    curNode = path[-1]
    realpath = []
    while curNode[2] != -1:
        realpath.append(curNode[0:2])
        curNode = path[curNode[2]]
    realpath.append(curNode[0:2])
    realpath.reverse()
    for node in realpath:
        print(node)

def deque_maze_path(x1 ,y1 ,x2 ,y2):
    queue = deque()     # 创建队列
    queue.append((x1,y1,-1))    # 先把起点放到队列中
    path = []   # 存放走的坐标
    while len(queue) > 0:
        curNode = queue.popleft()
        path.append(curNode)
        if curNode[0] == x2 and curNode[1] == y2:
            print_r(path)
            return True

        for dir in dirs:
            nextNode = dir(curNode[0], curNode[1])
            if maze[nextNode[0]][nextNode[1]] == 0:     #判断是否可以走
                queue.append((nextNode[0],nextNode[1],len(path)-1))    #将可以走的位置加入到队列中
                maze[nextNode[0]][nextNode[1]] = 2  # 将走过的位置改为2

    else:
        print('没有路！')
        return False

deque_maze_path(1, 1, 8, 8)
