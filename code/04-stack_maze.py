# _*_ coding: utf-8 _*_
# created by Stephen•Liu on 2022/3/17 21:33
'''
    栈实现走迷宫
'''

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


# (x1, y1)代表起点；(x2, y2)代表终点
def maze_path(x1 ,y1 ,x2 ,y2):
    stack = [(x1,y1)]
    while (len(stack)) > 0:
        curNode = stack[-1] #把当前节点存起来
        # 如果当前节点的x，y 等于 终点节点x，y说明已经到达终点
        if curNode[0] == x2 and curNode[1] ==y2:
            for s in stack:
                print(s)
            print(len(stack))
            return True

        for dir in dirs:
            nextNode = dir(curNode[0],curNode[1])
            # 如果下一个节点为0 说明可以走
            if maze[nextNode[0]][nextNode[1]] == 0:
                stack.append(nextNode)
                maze[nextNode[0]][nextNode[1]] = 2  #将走过的节点标识为2
                break

        #当上下左右都走不通时，就往回走
        else:
            stack.pop()
    else:
        print('没有路')
        return False

maze_path(1,1,8,8)


d_init = dirs[0](2,3)
print('dis_init=',d_init)

for m in maze:
    print(m)