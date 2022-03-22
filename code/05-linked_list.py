# _*_ coding: utf-8 _*_
# created by Stephen•Liu on 2022/3/22 20:10
'''
    单向链表
'''


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


# 查找到链表中值的对象
def select_node(lk, value):
    while lk:
        if lk.item == value:
            return lk
        lk = lk.next


# 向链表中插入新的对象
def insert_node(val_lk, node):
    node.next = val_lk.next
    val_lk.next = node


# 删除链表中的对象
def delete_node(lk, value):
    tmp = None
    while lk:
        if lk.item == value:
            tmp.next = lk.next
        tmp = lk
        lk = lk.next


li = [1, 2, 3, 4, 5]

lk = create_linklist_tail(li)
print_linklist(lk)

insert_node(select_node(lk, 3), Node(7))
print()
print_linklist(lk)
delete_node(lk, 7)
print()
print_linklist(lk)
