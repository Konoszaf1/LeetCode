from typing import List
import array

# Kinda terrible solution, but I got a headache
def counted_value(list1, value) -> int:
    return value if value not in list1 and list1.append(value) is None else 101

class Solution:
    def removeDuplicates(self, nums: List[int]) -> int:
        list1 = []
        copy = [x for x in nums]
        nums.clear()
        nums.extend(sorted([counted_value(list1, x) for x in copy]))
        return len(list1)


if __name__ == "__main__":
    nums = [0,0,1,1,1,2,2,3,3,4]
    print(Solution().removeDuplicates(nums))
    print(nums)