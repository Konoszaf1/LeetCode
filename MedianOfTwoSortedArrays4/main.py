import math
from typing import List

# Standard approach
class Solution:
    def findMedianSortedArrays(self, nums1: List[int], nums2: List[int]) -> float:
        nums = sorted(nums1 + nums2)
        length = len(nums)
        if length % 2 != 0:
            return nums[length // 2]
        else:
            num = nums[math.ceil((length / 2))]
            num1 = nums[math.floor((length / 2) - 1)]
            return (num + num1) / 2

if __name__ == "__main__":
    print(Solution().findMedianSortedArrays(nums1=[1, 2], nums2=[3, 4]))