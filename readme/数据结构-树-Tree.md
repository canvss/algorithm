# 树的概念
**树（Tree）是一种抽象数据类型，或是实现这种抽象数据类型的数据结构，用来模拟具有树状结构性质的数据集合。一般由N个有限节点组合，具有层次关系。**

![](https://canvs.oss-cn-chengdu.aliyuncs.com/canvs_typora/algorithm/tree.png)

**树是一种可以递归定义的数据结构**

**树是由n个节点组成的集合：**

- 如果n=0，那么这是一颗空树；
- 如果n>0，那存在1个节点作为树的根节点，其他节点可以分为m个集合，每个集合本身又是一棵树。

### 树具有的特点
 - 每个节点有零个或多个**子节点**
 - 没有父节点的节点称为**根**
 - 每个非根节点有且只有一个**父节点**
 - 除了根节点以外，每个子节点又可以分为多个不相交的子树

## 二叉树（Binary tree）
**二叉树是指树中节点的度不大于2(两颗子树)的有序树**

基于二叉树，又可分为**满二叉树**和**完全二叉树**

- 满二叉树

   一个二叉树，如果每一个层的结点树都达到最大值，则这个二叉树就是二叉树


- 完全二叉树

  若设二叉树的深度为h，除第h层外，其他各层（1～（h-1）层）的节点树都达到最大个数，第h层所有的节点都连续集中在最左边，这就是完全二叉树

![](https://canvs.oss-cn-chengdu.aliyuncs.com/canvs_typora/algorithm/tree-1.png)

### 二叉树的存储方法（表示方式）
- **链式存储方式**

- **顺序存储方式**

![](https://canvs.oss-cn-chengdu.aliyuncs.com/canvs_typora/algorithm/Figure-A7-Binary-tree-data-generating-structure-Note-that-the-tree-data-structure-is.png)

子节点和父节点的关系
- 父节点计算左子节点：**2i+1**
- 父节点计算右子节点：**2i+2**
- 子节点计算父节点下标：**（i-1）//2**

### 树的实例：模拟文件系统
```python
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
```

### 链表实现二叉树

```python
class BinaryTreeNode:
    def __init__(self ,data):
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
```

### 二叉树遍历
#### **前序遍历:**

首先访问根节点，然后遍历左子树，最后遍历右子树。

![](https://canvs.oss-cn-chengdu.aliyuncs.com/canvs_typora/algorithm/pre_order_traversal.gif)
```python
def pre_order(root):
    if root:
        print(root.data,end=', ')
        pre_order(root.lchild)
        pre_order(root.rchild)
```

#### **中序遍历**

先遍历左子树，然后访问根节点，然后遍历右子树。

![](https://canvs.oss-cn-chengdu.aliyuncs.com/canvs_typora/algorithm/in_order_traversal.gif)
```python
def in_order(root):
    if root:
       in_order(root.lchild)
       print(root.data, end=', ')
       in_order(root.rchild)
```

#### **后序遍历**

是先遍历左子树，然后遍历右子树，最后访问树的根节点。

![](https://canvs.oss-cn-chengdu.aliyuncs.com/canvs_typora/algorithm/post_order_traversal.gif)
```python
def post_order(root):
    if root:
        post_order(root.lchild)
        post_order(root.rchild)
        print(root.data, end = ', ')
```

#### **层次遍历**

层序遍历就是逐层遍历树结构。

![](https://canvs.oss-cn-chengdu.aliyuncs.com/canvs_typora/algorithm/level_order_traversal.gif)

```python
def level_order(root):
    queue = deque()
    queue.append(root)
    while len(queue) > 0:   # 只要队不空
        node = queue.popleft()
        print(node.data, end=', ')
        if node.lchild:
            queue.append(node.lchild)
        if node.rchild:
            queue.append(node.rchild)
```

## 二叉搜索树 
**二叉查找树（Binary Search Tree），（又：二叉搜索树，二叉排序树）它或者是一棵空树，或者是具有下列性质的二叉树： 若它的左子树不空，则左子树上所有结点的值均小于它的根结点的值； 若它的右子树不空，则右子树上所有结点的值均大于它的根结点的值； 它的左、右子树也分别为二叉排序树。二叉搜索树作为一种经典的数据结构，它既有链表的快速插入与删除操作的特点，又有数组快速查找的优势；所以应用十分广泛，例如在文件系统和数据库系统一般会采用这种数据结构进行高效率的排序与检索操作。**

![](https://canvs.oss-cn-chengdu.aliyuncs.com/canvs_typora/algorithm/bst.png)

### 二叉搜索树 -- 插入

二叉搜索树中的新节点总是添加到叶子位置。执行搜索可以轻松找到新节点的位置。

![](https://canvs.oss-cn-chengdu.aliyuncs.com/canvs_typora/algorithm/bst_insert.png)

```python
    def insert(self, node, val):
        if not node: 
            node = TreeNode(val)
            return node
        elif node.data < val: 
            node.rchild = self.insert(node.rchild, val)
            node.rchild.parent = node
        elif node.data > val: 
            node.lchild = self.insert(node.lchild, val)
            node.lchild.parent = node
        return node
```
### 二叉搜索树 -- 查询

- 从树的根节点开始
- 如果值小于当前节点，左移
- 如果值大于当前节点，向右移动

![](https://canvs.oss-cn-chengdu.aliyuncs.com/canvs_typora/algorithm/bst_query.png)
```python
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
```

### 二叉搜索树 -- 删除

- **如果要删除的节点是叶子节点**

   操作方法：直接删除

![](https://canvs.oss-cn-chengdu.aliyuncs.com/canvs_typora/algorithm/bst_delete-01.png)

```python
    def __remove_node_leaf(self, node):
        # 情况1：node是叶子节点
        if not node.parent:  # node为根节点
            self.root = None
        if node.parent.lchild == node:  # node是左孩子
            node.parent.lchild = None
        else:  # node是右孩子
            node.parent.rchild = None
```
  - **如果要删除的节点只有一个孩子**

     操作方法：将此节点的父亲与孩子连接，然后删除该节点

  ![](https://canvs.oss-cn-chengdu.aliyuncs.com/canvs_typora/algorithm/bst_delete-02.png)

```python
    def __remove_node_lchild(self, node):
        # node只有一个左孩子
        if not node.parent:  # node是根节点
            self.root = node.lchild
        elif node.parent.lchild == node:  # node是左孩子
            node.parent.lchild = node.lchild
            node.lchile.parent = node.parent
        else:  # node是右孩子
            node.parent.rchild = node.lchild
            node.lchile.parent = node.parent

    def __remove_node_rchild(self, node):
        # node只有一个右孩子
        if not node.parent:
            self.root = node.rchild
        elif node == node.parent.lchild:
            node.parent.lchild = node.rchild
            node.rchild.parent = node.parent
        else:
            node.parent.rchild = node.rchild
            node.rchild.parent = node.parent
```
  - **如果要删除的节点有两个孩子**
  
     操作方法：将其右子树最小节点删除，替换到当前节点

  ![](https://canvs.oss-cn-chengdu.aliyuncs.com/canvs_typora/algorithm/bst_delete-03.png)

```python
    def delete(self, val):
        if self.root:  # 树不空
            node = self.query_no_rec(val)
            if not node:
                return False
            if not node.lchild and not node.rchild:     # node是根节点
                self.__remove_node_leaf(node)
            elif not node.rchild:       # node只有一个左孩子
                self.__remove_node_lchild(node)
            elif not node.lchild:       # node只有一个右孩子
                self.__remove_node_rchild(node)
            else:
                min_node = node.rchild
                while min_node.lchild:     # 拿到右子树中最小的节点
                    min_node = min_node.lchild
                node.data = min_node.data   # 将右子树最小节点覆盖当前node
                if min_node.rchild:     # 只有右孩子
                    self.__remove_node_rchild(min_node)
                else:   # 叶子节点
                    self.__remove_node_leaf(min_node)
```

## 二叉搜索树的效率
- 平均情况下，二叉搜索树进行搜索的时间复杂度（O(lgn)）。
- 最坏情况下，二叉搜索树可能非常偏斜
- 解决方案：
  - 随机优化插入
  - AVL树



## AVL树

**AVL树是一颗自平衡的二叉搜索树。**

AVL树具有一下性质：
- **根的左右子树的高度之差的绝对值不能超过1**
- **根的左右子树都是平衡二叉树**

![](https://canvs.oss-cn-chengdu.aliyuncs.com/canvs_typora/algorithm/avl_tree.png)

### AVL树 --插入
- 插入一个节点可能会破坏AVL树的平衡，可以通过旋转操作来进行修正。
- 插入一个节点后，只有从插入节点到根节点的路径上的节点的平衡可能被改变。我们需要找出第一个破坏了平衡条件的节点，称之为K。k的两颗子树的高度差2.
- 不平衡的出现可能有4中情况

#### 左旋
不平衡是由于对K的右孩子的右子树插入导致的：左旋

![](https://canvs.oss-cn-chengdu.aliyuncs.com/canvs_typora/algorithm/avl_left.png)


#### 右旋
不平衡是由于对K的左孩子的左子树插入导致的：右旋

![](https://canvs.oss-cn-chengdu.aliyuncs.com/canvs_typora/algorithm/avl_right.png)


#### 右旋->左旋
不平衡是由对K的右孩子的左子树插入导致的

![](https://canvs.oss-cn-chengdu.aliyuncs.com/canvs_typora/algorithm/avl_right_left.png)

#### 左旋->右旋
不平衡是由于对K的左孩子的右子树插入导致的

![](https://canvs.oss-cn-chengdu.aliyuncs.com/canvs_typora/algorithm/avl_left_right.png)
