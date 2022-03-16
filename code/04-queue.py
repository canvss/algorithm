# _*_ coding: utf-8 _*_
# created by Stephen•Liu on 2022/3/16 22:15

class Queue:
    def __init__(self, size=100):
        # 创建一个队列
        self.queue = [0 for _ in range(size)]
        self.size = size
        self.front = 0  #队首指针
        self.rear = 0   #队尾指针

    # 向队列中插入数据
    def push(self, element):
        # 是否为满队列
        if not self.is_filled():
            self.rear = (self.rear + 1) % self.size
            self.queue[self.rear] = element
        else:
            raise IndexError('Queue is filled.')

    # 删除队列
    def pop(self):
        # 是否为空队列
        if not self.is_empty():
            self.front = (self.front + 1) % self.size
            return self.queue[self.front]
        else:
            raise IndexError('Queue is empty.')

    # 判断是否空队列
    def is_empty(self):
        return self.rear == self.front

    # 判断是否满队列
    def is_filled(self):
        return self.front == (self.rear + 1) % self.size

queue = Queue()
print(queue.is_empty())
for i in range(1, 5):
    queue.push(i)
print(queue.is_filled())
print(queue.pop())
queue.push(100)
