import math
import re
from typing import List


class Solution:
   # Solution can't account for increasing width accurately
   #  def maxArea(self, height: List[int]) -> int:
   #      previous_taller_index = 0
   #      left_col = height[0]
   #      left_col_index = 0
   #      surface = 0
   #      for index, column in enumerate(height):
   #          temp_surface = min(left_col, column) * (index - left_col_index)
   #          if temp_surface > surface:
   #              surface = temp_surface
   #          if column > left_col:
   #              temp_surface = min(height[previous_taller_index], column) * (index - previous_taller_index)
   #              if height[left_col_index] > height[previous_taller_index]:
   #                  previous_taller_index = left_col_index
   #              left_col = column
   #              left_col_index = index
   #          if temp_surface > surface:
   #              surface = temp_surface
   #      return surface

# Approach with sliding window
# Deemed not optimal, was expanding outward symmetric and would miss solutions
#     def maxArea(self, height: List[int]) -> int:
#         if len(height) % 2 == 0:
#             left_index = math.floor(len(height) / 2) - 1
#             right_index = math.ceil(len(height) / 2)
#         else:
#             left_index = math.floor(len(height) / 2)
#             right_index = left_index
#         surface = 0
#         while left_index >= 0 and right_index <= len(height) - 1:
#             temp_surface = min(height[left_index], height[right_index]) * (right_index - left_index)
#             if temp_surface >= surface:
#                 surface = temp_surface
#                 left_index -= 1
#                 right_index += 1
#             else:
#                 if left_index - 1 != 0 and height[left_index - 1] > height[left_index]:
#                     left_index -= 1
#                 if right_index + 1 <= len(height) - 1 and height[right_index + 1] > height[right_index]:
#                     right_index += 1
#         return surface


# Two converging pointers approach
    def maxArea(self, height: List[int]) -> int:
        left_index = 0
        right_index = len(height) - 1
        surface = 0
        while left_index <= right_index:
            temp_surface  = min(height[left_index], height[right_index]) * (right_index - left_index)
            if temp_surface > surface:
               surface = temp_surface
            if height[left_index] <= height[right_index]:
                left_index += 1
            else:
                right_index -= 1
        return  surface

if __name__ == "__main__":
    print(Solution().maxArea([1,8,6,2,5,4,8,3,7]))
    print(Solution().maxArea([1, 1]))
    print(Solution().maxArea([1,2,1]))
    print(Solution().maxArea([2, 1]))
    print(Solution().maxArea([1,2,3,4,5,6,7,8,9,10]))