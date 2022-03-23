# _*_ coding: utf-8 _*_
# created by Stephen•Liu on 2022/3/23 21:14


class LinkList:
    # 创建节点类
    class Node:
        def __init__(self, item):
            self.item = item
            self.next = None

    # 迭代器类
    class LinkListIterator:
        def __init__(self, node):
            self.node = node

        def __next__(self):
            if self.node:
                cur_node = self.node
                self.node = cur_node.next
                return cur_node.item
            else:
                raise StopIteration

        def __iter__(self):
            return self

    def __init__(self, iterable=None):
        '''
        构造函数
        :param iterable: 要插入链表数据的列表
        '''
        self.head = None
        self.tail = None
        if iterable:
            self.extend(iterable)

    def append(self, obj):
        '''
        插入节点
        :param obj: 要插入的值
        :return:
        '''
        s = LinkList.Node(obj)
        if not self.head:
            self.head = s
            self.tail = s
        else:
            self.tail.next = s
            self.tail = s

    def extend(self, iterable):
        for obj in iterable:
            self.append(obj)

    def find(self, obj):
        for n in self:
            if n == obj:
                return True
        else:
            return False

    def delete(self, value):
        node = self.head
        tmp = None
        while node:
            if node.item == value:
                tmp.next = node.next
                return True
            tmp = node
            node = node.next

    def __iter__(self):
        '''
        如果一个类想被用与循环迭代，就必须实现一个__iter__()方法，该方法返回一个迭代对象
        ，循环过程中会不断调用迭代对象的__next__()方法拿到下一个值。遇到StopIteration异常结束。
        :return:
        '''
        return self.LinkListIterator(self.head)

    def __repr__(self):
        return "【" + ", ".join(map(str, self)) + "】"


class HashTable:
    def __init__(self, size=10):
        self.size = size
        # 创建一个<LinkList>类型的空列表
        self.T = [LinkList() for _ in range(self.size)]

    # hash函数
    def hash(self, k):
        return k % self.size

    def insert(self, k):
        i = self.hash(k)
        if self.find(k):
            print("重复插入")
        else:
            self.T[i].append(k)

    def delete(self, k):
        i = self.hash(k)
        return self.T[i].delete(k)

    def find(self, k):
        i = self.hash(k)
        return self.T[i].find(k)


ht = HashTable()
ht.insert(1)
ht.insert(2)
ht.insert(3)
ht.insert(11)
# ht.insert(1)
print(ht.find(3))
# print(",".join(map(str, ht.T)))
print(",".join(map(str, ht.T)))

ht.delete(11)
print(",".join(map(str, ht.T)))
