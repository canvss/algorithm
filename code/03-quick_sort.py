# _*_ coding: utf-8 _*_
# created by Stephen•Liu on 2022/3/8 23:15

'''
    快速排序
'''

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


li = [5,7,4,8,2,6,1,9,3]
print(li)
quick_sort(li,0,len(li)-1)
print(li)