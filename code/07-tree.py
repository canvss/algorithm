# _*_ coding: utf-8 _*_
# created by Stephen•Liu on 2022/3/24 20:01

class Node:
    def __init__(self, name, type='dir'):
        self.name = name
        self.type = type
        self.children = []
        self.parent = None

    def __repr__(self):
        return self.name


class FileSystemTree:
    def __init__(self):
        self.root = Node("/")
        self.pwd = self.root

    def mkdir(self, name):
        if name[-1] != '/':
            name += '/'
        node = Node(name)
        node.parent = self.pwd
        self.pwd.children.append(node)

    def cd(self, name):
        if name == '..':
            self.pwd = self.pwd.parent
            return

        if name[-1] != '/':
            name += '/'
        for child in self.pwd.children:
            if child.name == name:
                self.pwd = child
                return
        raise ValueError('找不到目录...')

    def ls(self):
        return self.pwd.children

tree = FileSystemTree()
tree.mkdir('usr')
tree.mkdir('etc/')
tree.mkdir('bin')
print(tree.ls())
tree.cd('bin')
tree.mkdir('java')
tree.mkdir('python')
print(tree.ls())
tree.cd('..')
print(tree.ls())
