import dis
from typing import List
import heapq
# Sliding window approach, realized that indices are a subset and not a subarray
# class Solution:
#     def maxScore(self, nums1: List[int], nums2: List[int], k: int) -> int:
#         score = 0
#         for i in range(0, len(nums1)-k):
#             tmp = sum(nums1[i:k+i]) * min(nums2[i:k+i])
#             if tmp > score:
#                 score = tmp
#         return score

class Solution:
    def maxScore(self, nums1: List[int], nums2: List[int], k: int) -> int:
        pairs = sorted(zip(nums1,nums2), key=lambda i: -i[1])
        heap = []
        heapq.heapify(heap)
        summ = 0
        best = 0
        for pair in pairs:
            if len(heap) < k:
                heapq.heappush(heap, pair[0])
                summ += pair[0]
            elif pair[0] > heap[0]:
                summ += (pair[0] - heap[0])
                heapq.heapreplace(heap, pair[0])
            else:
                continue
            if len(heap) == k:
                best = max(best, pair[1] * summ)
        return best




if __name__ == "__main__":
    print(Solution().maxScore([1,3,3,2], [2,1,3,4], 3))
    print(Solution().maxScore([4,2,3,1,1], [7,5,10,9,6], 1))