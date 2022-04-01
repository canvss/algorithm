# _*_ coding: utf-8 _*_
# created by Stephen•Liu on 2022/3/30 20:43

from collections import deque


class BinaryTreeNode:
    def __init__(self, data):
        self.data = data
        self.lchild = None
        self.rchild = None


E = BinaryTreeNode('E')
A = BinaryTreeNode('A')
G = BinaryTreeNode('G')
C = BinaryTreeNode('C')
F = BinaryTreeNode('F')
B = BinaryTreeNode('B')
D = BinaryTreeNode('D')

root = E
E.lchild = A
E.rchild = G
A.rchild = C
C.rchild = D
C.lchild = B
G.rchild = F


def pre_order(root):
    if root:
        print(root.data, end=', ')
        pre_order(root.lchild)
        pre_order(root.rchild)


def in_order(root):
    if root:
        in_order(root.lchild)
        print(root.data, end=', ')
        in_order(root.rchild)


def post_order(root):
    if root:
        post_order(root.lchild)
        post_order(root.rchild)
        print(root.data, end=', ')


def level_order(root):
    queue = deque()
    queue.append(root)
    while len(queue) > 0:  # 只要队不空
        node = queue.popleft()
        print(node.data, end=', ')
        if node.lchild:
            queue.append(node.lchild)
        if node.rchild:
            queue.append(node.rchild)


# pre_order(root)
# in_order(root)
# post_order(root)
level_order(root)
