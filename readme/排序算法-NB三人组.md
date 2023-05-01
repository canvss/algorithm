## 快速排序(Quicksort) 时间复杂度：o(N*logN)

**快速排序，又称划分交换排序（partition-exchange sort），简称快排，一种排序算法，最早由东尼·霍尔提出。在平均状况下，排序n个项目要O(n log2 n)次比较。在最坏状况下则需要 O(n^2)次比较，但这种状况并不常见。事实上，快速排序 (n log n)通常明显比其他算法更快，因为它的内部循环（inner loop）可以在大部分的架构上很有效率地达成。**

![](https://canvs.oss-cn-chengdu.aliyuncs.com/canvs_typora/algorithm/Quicksort_img.gif)

### 快速排序思路：

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

![](https://canvs.oss-cn-chengdu.aliyuncs.com/canvs_typora/algorithm/quick_sort2.png)

### 快速排序的最坏情况

 - 列表已按相同顺序排序
 - 列表已按相反顺序排序
 - 所有元素都相同（情况1和情况2的特例）

**解决办法：随机选取中心轴下标。**

## 堆排序
**堆排序（英语:Heapsort）是指利用堆这种数据结构所设计的一种排序算法。堆是一个近似完全二叉树的结构，并同时满足堆积的性质：即子结点的键值或索引总是小于（或者大于）它的父节点**

### 什么是堆（heap）
**堆：一种特殊的完全二叉树结构**

- 大根堆：一颗完全二叉树，满足任一节点都比其孩子节点大
- 小根堆：一颗完全二叉树，满足任一节点都比其孩子节点小

![](https://canvs.oss-cn-chengdu.aliyuncs.com/canvs_typora/algorithm/heap.png)

### 堆的向下调整

**根节点的左右子树都是堆，根节点所在的树自身不是堆。可以通过一次向下调整变成一个堆。**

- 若想将其调整为小堆，那么根结点的左右子树必须都为小堆。
- 若想将其调整为大堆，那么根结点的左右子树必须都为大堆。

![](https://canvs.oss-cn-chengdu.aliyuncs.com/canvs_typora/algorithm/heap-down.gif)

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

### 堆排序的实现 时间复杂度o（nlogn）
- 将最后一个元素和堆顶交换位置，每次将最后一个元素向前移动一位
- 做堆的向下调整

![](https://canvs.oss-cn-chengdu.aliyuncs.com/canvs_typora/algorithm/heap_sort.gif)
```python
def heap_sort(li):
    n = len(li)
    # 构建堆
    for i in range((n-2)//2,-1,-1): #i表示建堆时部分根下标
        sift(li,i,n-1)  #将堆的最后一个元素作为high
    for i in range(n-1 ,-1 ,-1):    #i指当前堆的最后一个元素
        li[i] ,li[0] = li[0] ,li[i] #把当前堆顶和堆的最后一个元素交换位置
        sift(li ,0 ,i - 1)
```

### 堆排序的应用（topk ）
#### 现在有n个数，设计算法得到前k大的数？（k<n）

**解决思路：**

- 排序后切片       o(nlogn)
- 排序LowB三人组   o(kn)
- 堆排序          o(nlogk)
  - 取列表前k个元素建立一个小根堆。堆顶就是目前第k大的数；
  - 依次向后遍历原列表，对于列表中的元素，如果小于堆顶，则忽略该元素；如果大于堆顶，则将堆顶更换为该元素，并且对堆进行依次调整；
  - 遍历列表所有元素后，倒序弹出堆顶

```python
# 构建小根堆
def sift(li,low,high):
    i = low
    j = 2 * i +1
    tmp = li[i]
    while j <= high:
        if j+1 <= high and li[j+1] < li[j]:
            j +=1
        if li[j] < tmp:
            li[i] = li[j]
            i = j
            j = 2*i+1
        else:
            break
    li[i] = tmp

def heap_topk(li,k):
    heap = li[0:k]
    for i in range((k-2)//2 ,-1 ,-1):
        sift(heap ,i ,k-1)

    # 1、构建堆
    for i in range(k ,len(li)-1):
        if li[i] > heap[0]:
            heap[0] = li[i]
            sift(heap,0,k-1)

    #2、遍历
    for i in range(k-1 ,-1 ,-1):
        heap[0] ,heap[i] = heap[i] ,heap[0]
        sift(heap ,0 ,i-1)

    # 出数
    return heap
```

## 归并排序 

**归并排序（英语：Merge sort，或mergesort），是创建在归并操作上的一种有效的排序算法。1945年由约翰·冯·诺伊曼首次提出。该算法是采用分治法（Divide and Conquer）的一个非常典型的应用，且各层分治递归可以同时进行。**

- 时间复杂度o(n*logn) 
- 空间复杂度o(n)

**归并排序思路：**

- 分解
- 排序
- 归并

### 归并

**将两个有序列表，归并成一个有序的列表**

![](https://canvs.oss-cn-chengdu.aliyuncs.com/canvs_typora/algorithm/merge.webp)

```python
def merge(li ,low ,mid ,high):
    i = low
    j = mid+1
    ltmp = []   # 用于临时存放排序好的列表
    # 左右两边都有数
    while i <= mid and j <= high:   # 如果左边部分小于mid并且右边部分小于high
        if li[i] < li[j]:   # 选出左右两边小的值
            ltmp.append(li[i])  # 将左边值添加到新的列表
            i += 1  # 将下标往后移动
        else:
            ltmp.append(li[j])
            j += 1
    # 有可能右边没数，但左边还有数
    while i <= mid:
        ltmp.append(li[i])
        i += 1
    # 有可能左边没数，但右边还有数
    while j <= high:
        ltmp.append(li[j])
        j += 1
    li[low:high+1] = ltmp
```
### 归并排序实现

**归并排序的核心思想其实很简单，如果要排序一个列表，我们先把列表从中间分成前后两部分，然后分别对前后两部分进行排序，再将排好序的两部分数据合并在一起就可以了。**

![](https://canvs.oss-cn-chengdu.aliyuncs.com/canvs_typora/algorithm/merge_sort.png)

```python
def merge_sort(li ,low ,high):
    if low < high:      #至少有两个数
        mid = (low + high)//2
        merge_sort(li,low,mid)
        merge_sort(li,mid+1,high)
        merge(li ,low ,mid ,high)
```



## NB三人组总结

**三种排序算法的时间复杂度都是O(nlogn)**

**一般情况下，就运行时间而言：**

- 快速 < 归并 < 堆排序

**三种排序算法的缺点：**

- 快速排序：极端情况下排序效率低
- 归并排序：需要额外的内存开销
- 堆排序：在快的排序算法中相对较慢
