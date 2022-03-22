# _*_ coding: utf-8 _*_
# created by Stephen•Liu on 2022/3/22 20:10

class Node:
    def __init__(self, item):
        self.item = item
        self.next = None


# 头插法
def create_linklist_head(li):
    head = Node(li[0])
    for element in li[1:]:
        node = Node(element)
        node.next = head
        head = node
    return head


# 尾插法
def create_linklist_tail(li):
    head = Node(li[0])
    tail = head
    for element in li[1:]:
        node = Node(element)
        tail.next = node
        tail = node
    return head


# 打印链表
def print_linklist(lk):
    while lk:
        print(lk.item, end=',')
        lk = lk.next


li = [1, 2, 3, 4, 5]
lk = create_linklist_head(li)
print_linklist(lk)

lk2 = create_linklist_tail(li)
print()
print_linklist(lk2)
