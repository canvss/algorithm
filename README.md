![](imgs/img.png)

# 算法&数据结构
### 时间复杂度（Time complexity)
在计算机科学中，算法的时间复杂度（Time complexity）是一个函数，它定性描述该算法的运行时间。
### 空间复杂度(Space Complexity)
在计算机科学中，一个算法或程序的空间复杂度定性地描述该算法或程序运行所需要的存储空间大小。



## 一、递归
程序调用自身的编程技巧称为递归（ recursion）。递归作为一种算法在程序设计语言中广泛应用。 一个过程或函数在其定义或说明中有直接或间接调用自身的一种方法，它通常把一个大型复杂的问题层层转化为一个与原问题相似的规模较小的问题来求解，递归策略只需少量的程序就可描述出解题过程所需要的多次重复计算，大大地减少了程序的代码量。递归的能力在于用有限的语句来定义对象的无限集合。一般来说，递归需要有边界条件、递归前进段和递归返回段。当边界条件不满足时，递归前进；当边界条件满足时，递归返回。

![](imgs/recursion2.png)

```python
def recursion(i):
    if i > 0:
        print(i)
        recursion(i-1)
recursion(3)
# 输出结果：1、2、3
```

![](imgs/recursion.png)

```python
def recursion2(i):
    if i > 0:
        recursion2(i-1)
        print(i)
# 输出结果：3、2、1
```

### 汉诺塔
   法国数学家爱德华·卢卡斯曾编写过一个印度的古老传说：在世界中心贝拿勒斯（在印度北部）的圣庙里，一块黄铜板上插着三根宝石针。印度教的主神梵天在创造世界的时候，在其中一根针上从下到上地穿好了由大到小的64片金片，这就是所谓的汉诺塔。不论白天黑夜，总有一个僧侣在按照下面的法则移动这些金片：一次只移动一片，不管在哪根针上，小片必须在大片上面。僧侣们预言，当所有的金片都从梵天穿好的那根针上移到另外一根针上时，世界就将在一声霹雳中消灭，而梵塔、庙宇和众生也都将同归于尽。

![](imgs/hanoi.gif)

 - 1、把n-1个盘子从a通过c移动到b
 - 2、把第n个盘从a移动到c
 - 3、把n-1个盘子从b通过a移动到c

```python
def hanoi(n,a,b,c):
    if n > 0:
        hanoi(n-1,a,c,b)
        print(('moving %s from %s'),(a,c))
        hanoi(n-1,b,a,c)

hanoi(3,'A','B','C')
```



## 二、常用查找与排序算法
### 顺序查找(Linear Search)  时间复杂度：o(n)
顺序查找：也叫线性查找，从列表第一个元素开始，顺序进行搜索，知道找到元素或搜索到列表最后一个元素为止。

![](imgs/linear_search.gif)

```python
def linear_search(li,val):
    for i,v in enumerate(li):
        if v == val:
            return i
    else:
         return None
```

### 二分查找法（binary_search） 时间复杂度：O（log2n）
在一个已知有序队列中找出与给定关键字相同的数的具体位置。原理是分别定义三个指针low、high、mid分别指向待查元素所在范围的下界和上界以及区间的中间位置，即mid＝（low＋high）/2，让关键字与mid所指的数比较，若等则查找成功并返回mid，若关键字小于mid所指的数则high=mid-1，否则low=mid+1，然后继续循环直到找出或找不到为止。

![](imgs/binary_search.gif)

````python
def binary_search(li,val):
    left = 0
    right = len(li) - 1
    while right >= left:    #候选区有值
        mid = (left + right) // 2
        if li[mid] == val:
            return mid
        elif li[mid] > val:  #候选区在mid左边
            right = mid - 1
        else:   #li[mid] < val 候选区在mid右边
            left = mid + 1
    else:
        return None
````



## 三、排序
排序也称排序算法(Sort Algorithm)，排序是将一组数据，依指定的顺序进行排列的过程。

### 冒泡排序（Bubble Sort) 时间复杂度：o(n^2)
 - 比较相邻的元素。如果第一个比第二个大，就交换他们的位置。

![](imgs/bubblesort.gif)

```python
def bubble_sort(li):
    for i in range(len(li) - 1):    #第i躺
        exchange = False
        for j in range(len(li) - i -1):
            if li[j] > li[j+1]:
                li[j],li[j+1] = li[j+1],li[j]   #交换位置
                exchange = True
        if not exchange:
            return
```

### 选择排序（Selection sort）时间复杂度：O(n^2)
首先在未排序序列中找到最小（大）元素，存放到排序序列的起始位置，然后，再从剩余未排序元素中继续寻找最小（大）元素，然后放到已排序序列的末尾。以此类推，直到所有元素均排序完毕。

![](imgs/selection-sort.gif)

```python
def selection_sort(li):
    for i in range(len(li)-1):    #第i趟
        min_loc = i
        for j in range(i+1,len(li)):
            if li[j] < li[min_loc]:
                min_loc = j     #将最小值赋值给min_loc
        li[min_loc] , li[i] = li[i] , li[min_loc]   #待排序区域最小值放到元素开始下标
```

### 插入排序（Insertion sort） 时间复杂度：o(n^2)
假设你在玩扑克牌，你要把牌按从小到大排列。当你拿到第一张牌，那它就是最小的，把它放在第一个位置上。当你拿到第二张牌，你和第一张牌做比较，如果它大于第一张牌，则把它放到第一张牌的右边，反之则放到左边。当你拿到第三张牌，你拿它和第二个位置上的牌比较，然后如有必要需要和第一个位置上的牌比较。然后是第四张牌……最后，一手牌就按从小到大的顺序排好了。这就是插入排序。 在其实现过程使用双层循环，外层循环对除了第一个元素之外的所有元素，内层循环对当前元素前面有序表进行待插入位置查找，并进行移动

![](imgs/insertion_sort.gif)

```python
def insert_sort(li):
    for i in range(1,len(li)):  #i为发到手上的牌
        tmp = li[i] 
        j = i - 1   #手上的牌
        while j >= 0 and li[j] > tmp:   #将大的牌向右移
            li[j+1] = li[j]
            j -= 1
        li[j+1] = tmp
```

### 快速排序(Quicksort) 时间复杂度：o(N*logN)
快速排序，又称划分交换排序（partition-exchange sort），简称快排，一种排序算法，最早由东尼·霍尔提出。在平均状况下，排序n个项目要O(n log2 n)次比较。在最坏状况下则需要 O(n^2)次比较，但这种状况并不常见。事实上，快速排序 (n log n)通常明显比其他算法更快，因为它的内部循环（inner loop）可以在大部分的架构上很有效率地达成。

![](imgs/Quicksort_img.gif)

快速排序思路：
   - 取一个元素p(第一个元素)，使元素p归位
   - 列表被p分成两部分，左边都比p小，右边都比p大
   - 递归完成排序

```python
def partition(li, left, right):
    tmp = li[left]
    while left < right:
        while left < right and li[right] >= tmp:    #从右边开始找比tmp小的数
            right -= 1  #向左走一步
        li[left] = li[right]    #把右边小于tmp的值写到左边空位上
        while left < right and li[left] <= tmp:     #从左边开始找比tmp大的数
            left += 1  #向右走一步
        li[right] = li[left]    #把左边大于tmp的值写到左边空位上
    li[left] = tmp  #将tmp归位
    return left

def quick_sort(li, left, right):
    if left < right:
        mid = partition(li,left,right)
        quick_sort(li, left, mid-1)
        quick_sort(li, mid+1,right)
```

![](imgs/quick_sort2.png)

快速排序的最坏情况
 - 列表已按相同顺序排序
 - 列表已按相反顺序排序
 - 所有元素都相同（情况1和情况2的特例）

解决办法：随机选取中心轴下标。

### 堆排序
堆排序（英语:Heapsort）是指利用堆这种数据结构所设计的一种排序算法。堆是一个近似完全二叉树的结构，并同时满足堆积的性质：即子结点的键值或索引总是小于（或者大于）它的父节点

#### 关于树
树（Tree）是一种抽象数据类型，或是实现这种抽象数据类型的数据结构，用来模拟具有树状结构性质的数据集合。一般由N个有限节点组合，具有层次关系。

![](imgs/tree.png)

树是一种可以递归定义的数据结构

树是由n个节点组成的集合：
- 如果n=0，那么这是一颗空树；
- 如果n>0，那存在1个节点作为树的根节点，其他节点可以分为m个集合，每个集合本身又是一棵树。

#### 树具有的特点
 - 每个节点有零个或多个子节点
 - 没有父节点的节点称为根
 - 每个非根节点有且只有一个父节点
 - 除了根节点以外，每个子节点又可以分为多个不相交的子树

#### 二叉树（Binary tree）
二叉树是指树中节点的度不大于2(两颗子树)的有序树

基于二叉树，又可分为满二叉树和完全二叉树

- 满二叉树

   一个二叉树，如果每一个层的结点树都达到最大值，则这个二叉树就是二叉树


- 完全二叉树

  若设二叉树的深度为h，除第h层外，其他各层（1～（h-1）层）的节点树都达到最大个数，第h层所有的节点都连续集中在最左边，这就是完全二叉树

![](imgs/tree-1.png)

#### 二叉树的存储方法（表示方式）
- 链式存储方式

- 顺序存储方式

![](imgs/Figure-A7-Binary-tree-data-generating-structure-Note-that-the-tree-data-structure-is.png)

子节点和父节点的关系
- 父节点计算左子节点：2i+1
- 父节点计算右子节点：2i+2
- 子节点计算父节点下标：（i-1）//2

#### 什么是堆（heap）
堆：一种特殊的完全二叉树结构
- 大根堆：一颗完全二叉树，满足任一节点都比其孩子节点大
- 小根堆：一颗完全二叉树，满足任一节点都比其孩子节点小

![](imgs/heap.png)

#### 堆的向下调整
根节点的左右子树都是堆，根节点所在的树自身不是堆。可以通过一次向下调整变成一个堆。
- 若想将其调整为小堆，那么根结点的左右子树必须都为小堆。
- 若想将其调整为大堆，那么根结点的左右子树必须都为大堆。

![](imgs/heap_down.jpeg)

```python
def sift(li,low,high):
    """
    :param li: 列表
    :param low: 堆的根节点位置
    :param high: 堆最后一个元素的位置
    :return:
    """
    i = low #i最开始指向根节点
    j = 2 * i + 1   #j是左孩子
    tmp = li[low]     #将堆顶的值存起来
    while j <= high:    #j的值不能超过堆的最后一个元素
        if j + 1 <= high and li[j+1] > li[j]: #如果有右孩子并且比左孩子大，就把j指向右孩子
            j += 1
        if li[j] > tmp: #如果孩子大于堆顶，就交换他们的位置
            li[i] = li[j]
            i = j       #将i指向新的堆顶，向下看一层
            j = 2 * i +1    #根据堆顶求出左孩子
        else:
            break
    li[i] = tmp #如果j超过了high，或者孩子小于堆顶，就把tmp放回原位置
```

#### 堆排序的实现 时间复杂度o（nlogn）
- 将最后一个元素和堆顶交换位置，每次将最后一个元素向前移动一位
- 做堆的向下调整

![](imgs/min-binary-heap-extract-min.gif)

```python
def heap_sort(li):
    n = len(li)
    # 构建堆
    for i in range((n-2)//2,-1,-1): #i表示建堆时部分根下标
        sift(li,i,n-1)  #将堆的最后一个元素作为high
    print(li)
    for i in range(n-1 ,-1 ,-1):    #i指当前堆的最后一个元素
        li[i] ,li[0] = li[0] ,li[i] #把当前堆顶和堆的最后一个元素交换位置
        sift(li ,0 ,i - 1)
```



