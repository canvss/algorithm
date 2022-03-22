# _*_ coding: utf-8 _*_
# created by Stephen•Liu on 2022/3/22 23:12

class Node:
    def __init__(self, item):
        self.item = item
        self.next = None
        self.prior = None


def create_linked_list(li):
    head = Node(li[0])
    tail = head
    for element in li[1:]:
        node = Node(element)
        node.prior = tail
        tail.next = node
        tail = tail.next
    return head

li = [1,2,3,4,5,6]
lk = create_linked_list(li)
print(lk.item)
print(lk.next.item)
print(lk.next.prior.item)