from typing import List


# class Solution:
#     def minOperations(self, nums: List[int], k: int) -> int:
#         operations = 0
#         for num in nums:
#             if num < k:
#                 operations += 1
#         return operations

# What if we used list comprehension and/or cpython mapping

class Solution:
    def minOperations(self, nums: List[int], k: int) -> int:
        return sum(map(k.__gt__, nums))

if __name__ == "__main__":
    print(Solution().minOperations([2,11,10,1,3],10))
    print(Solution().minOperations([1,1,2,4,9],1))
    print(Solution().minOperations([1,1,2,4,9],9))