# _*_ coding: utf-8 _*_
# created by Stephen•Liu on 2022/3/14 23:19
from typing import List


class two_Sum:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        li =[]
        for i in range(len(nums)):
            for j in range(i+1,len(nums)):
                if nums[j]+nums[i] == target:
                    li.append(j)
                    li.append(i)
                    return li

