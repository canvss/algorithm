# _*_ coding: utf-8 _*_
# created by Stephen•Liu on 2022/4/1 20:00

class TreeNode:
    def __init__(self, data):
        self.data = data
        self.lchild = None
        self.rchild = None
        self.parent = None


class BST:
    def __init__(self, li=None):
        self.root = None
        if li:
            for var in li:
                self.insert_no_rec(var)

    # 递归查询
    def query(self, node, val):
        if not node:    # 判断空树
            return None
        if node.data == val:
            return node
        elif node.data > val:
            return self.query(node.lchild, val)
        elif node.data < val:
            return self.query(node.rchild, val)
        else:
            return None

    # 非递归查询
    def query_no_rec(self, val):
        p = self.root
        while p:
            if p.data == val:
                return p
            elif p.data > val:
                p = p.lchild
            elif p.data < val:
                p = p.rchild
        return None     # 树空

    # 递归插入
    def insert(self, node, val):
        if not node:  # 空树
            node = TreeNode(val)
            return node
        elif node.data < val:  # 往右边走
            node.rchild = self.insert(node.rchild, val)
            node.rchild.parent = node
        elif node.data > val:  # 往左边走
            node.lchild = self.insert(node.lchild, val)
            node.lchild.parent = node
        return node

    # 非递归插入
    def insert_no_rec(self, val):
        p = self.root
        if not p:  # 空树
            self.root = TreeNode(val)
            return
        while True:
            if p.data > val:  # 往左走
                if p.lchild:  # 左孩子有树
                    p = p.lchild
                else:
                    p.lchild = TreeNode(val)
                    p.lchild.parent = p
                    return
            elif p.data < val:  # 往右走
                if p.rchild:  # 右孩子有树
                    p = p.rchild
                else:
                    p.rchild = TreeNode(val)
                    p.rchild.parent = p
                    return
            else:
                return

    def pre_order(self, root):
        if root:
            print(root.data, end=', ')
            self.pre_order(root.lchild)
            self.pre_order(root.rchild)

    def in_order(self, root):
        if root:
            self.in_order(root.lchild)
            print(root.data, end=', ')
            self.in_order(root.rchild)

    def post_order(self, root):
        if root:
            self.post_order(root.lchild)
            self.post_order(root.rchild)
            print(root.data, end=', ')


tree = BST([5, 7, 4, 9, 2, 1, 3, 6, 8])
tree.pre_order(tree.root)
tree.insert(tree.root, 10)
print()
tree.in_order(tree.root)
print()
print(tree.query_no_rec(1))
