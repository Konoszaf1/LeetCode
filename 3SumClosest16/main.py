import heapq

class Solution:
    def threeSumClosest(self, nums: list[int], target: int) -> int:
        nums.sort()

        minimum = nums[0] + nums[1] + nums[2]

        for i in range(len(nums) - 2):
            left = i + 1
            right = len(nums) - 1

            while left < right:
                result = nums[i] + nums[left] + nums[right]

                if abs(result - target) < abs(minimum - target):
                    minimum = result

                if result == target:
                    return result
                elif result > target:
                    right -= 1
                else:
                    left += 1

        return minimum


if __name__ == "__main__":
    l2 = Solution().threeSumClosest([-1,2,1,-4,0,1,0], 1)
    l3 = Solution().threeSumClosest([1,1,1,0], -100)
    l4 = Solution().threeSumClosest([4,0,5,-5,3,3,0,-4,-5], -2)
    print(l2)
    print(l3)
    print(l4)