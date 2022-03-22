# _*_ coding: utf-8 _*_
# created by Stephen•Liu on 2022/3/22 21:52

class Node:
    def __init__(self, item):
        self.item = item
        self.next = Node
        # self.prior = Node


def create_linklist(li):
    head = Node(li[0])
    tail = head
    for element in li[1:]:
        node = Node(element)
        tail.next = node
        tail = node
    return head


def print_linklist(lk):
    while lk:
        print(lk.item, end=',')
        lk = lk.next




li = [1, 2, 3, 4, 5, 6]
lk = create_linklist(li)
print_linklist(lk)
