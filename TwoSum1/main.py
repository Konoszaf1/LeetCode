from typing import List


class Solution:
    # Too slow, iterates twice over nums
    # def twoSum(self, nums: List[int], target: int) -> List[int]:
    #     for index, num in enumerate(nums):
    #         for index1, num1 in enumerate(nums):
    #             if index != index1 and num + num1 == target:
    #                 return [index, index1]

    # Τhrow a hashmap at the problem (and dict comprehension ;))
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        dic = {x[1]: x[0] for x in enumerate(nums)}
        for x in enumerate(nums):
            if target - x[1] in dic and dic[target - x[1]] != x[0]:
                return dic[target-x[1]], x[0]



if __name__ == "__main__":
    print(Solution().twoSum(nums=[2, 3, 4], target=6))