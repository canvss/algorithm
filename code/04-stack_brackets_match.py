# _*_ coding: utf-8 _*_
# created by Stephen•Liu on 2022/3/15 21:33

'''
    栈的应用括号的匹配
'''

class Stack:
    def __init__(self):
        self.stack = []

    def push(self,element):
        self.stack.append(element)

    def pop(self):
        return self.stack.pop()

    def gettop(self):
        if len(self.stack) > 0:
            return self.stack[-1]
        else:
            return None

    def is_empty(self):
        return len(self.stack) == 0

def brackets_match(str):
    brackets = {'}':'{', ']':"[", ')':'('}
    stack = Stack()
    for ch in str:
        # 查看ch是否存在'(','[','{'
        if ch in {'(','[','{'}:
            stack.push(ch)
        else:
            if stack.is_empty():
                return False
            # 拿栈顶和当前值比较
            elif stack.gettop() == brackets[ch]:
                stack.pop()
            else:   #if stack.pop() != brackets[ch]
                return False
    # 如果列表为空返回true
    if stack.is_empty():
        return True
    else:
        return False

print(brackets_match('[{()}(){()}[]({}){}]'))
print(brackets_match('[]}'))