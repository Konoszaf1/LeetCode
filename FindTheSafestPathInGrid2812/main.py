# Solution below tried a cumulative thief danger map, that was not the correct approach
from collections import deque
from typing import List
#
# def get_distance(x, y, x1, y1) -> int:
#     return abs(x - x1) + abs(y - y1)
#
# def create_grid(dimension):
#     return [[0]*dimension for x in range(dimension)]
#
# def get_distance_from_thief_grid(thief_x, thief_y, grid) ->  List[List[int]]:
#     for i in  range(len(grid)):
#         for j in range(len(grid)):
#             grid[i][j] = get_distance(i, j, thief_x, thief_y)
#     return grid
#
# def add_lists(*lists, grid):
#     for i, row in enumerate(lists[0][0]):
#         for j, col in enumerate(lists[0][0]):
#             grid[i][j] = sum([x[i][j] for x in lists[0]])
#     return grid
#
# def find_minimum(thief_danger, thieves):
#     i = 0
#     j = 0
#     minimum = min([get_distance(*x, i, j) for x in thieves])
#     prev = False
#     while i != len(thief_danger) - 1 or j != len(thief_danger) - 1:
#         # Check if thief
#         if [i,j] in thieves:
#             minimum = 0
#             return minimum
#         # Boundary
#         if i == len(thief_danger) - 1:
#             if [i,j+1] in thieves:
#                 thieves.append([i, j])
#                 i -= 1
#             else:
#                 j += 1
#         elif j == len(thief_danger) - 1:
#             if [i+1,j] in thieves:
#                 thieves.append([i, j])
#                 j -= 1
#             else:
#                 i += 1
#         elif [i+1, j] in thieves and [i,j+1] in thieves and i==j==0:
#             return 0
#         elif [i+1, j] in thieves:
#             if [i, j + 1] in thieves:
#                 thieves.append([i, j])
#                 if i != 0:
#                     i -= 1
#                 else:
#                     j -= 1
#             else:
#                 j += 1
#         elif [i,j+1] in thieves:
#             if [i + 1, j] in thieves:
#                 thieves.append([i, j])
#                 if j != 0:
#                     j -= 1
#                 else:
#                     i -= 1
#             else:
#                 i += 1
#         elif thief_danger[i][j+1] == thief_danger[i+1][j]:
#             if not prev:
#                 j += 1
#                 prev = True
#             else:
#                 i += 1
#                 prev = False
#         elif thief_danger[i][j+1] > thief_danger[i+1][j]:
#             j += 1
#         elif thief_danger[i][j + 1] < thief_danger[i + 1][j]:
#             i += 1
#         temp = min([get_distance(*x, i, j) for x in thieves])
#         if temp < minimum:
#             minimum = temp
#     return minimum
#
# class Solution:
#     def maximumSafenessFactor(self, grid: List[List[int]]) -> int:
#         thieves = []
#         for i, row in enumerate(grid):
#             for j, col in enumerate(grid):
#                 if grid[i][j] == 1:
#                     thieves.append([i,j])
#         thief_grids=[]
#         for thief in thieves:
#             thief_grids.append(get_distance_from_thief_grid(*thief,create_grid(len(grid))))
#         total_thief_grid = add_lists(thief_grids, grid=create_grid(len(grid)))
#         pprint.pprint(total_thief_grid, width=150)
#         return find_minimum(total_thief_grid, thieves)

import heapq
def get_distance(x, y, x1, y1) -> int:
    return abs(x - x1) + abs(y - y1)

def create_grid(dimension):
    return [[0]*dimension for x in range(dimension)]

def create_thief_heatmap(thieves, grid):
    n = len(grid)

    safeness_grid = [[-1] * n for _ in range(n)]
    queue = deque()

    for r in range(n):
        for c in range(n):
            if grid[r][c] == 1:
                safeness_grid[r][c] = 0
                queue.append((r, c))
        directions = [(-1, 0), (1, 0), (0, -1), (0, 1)]

        while queue:
            r, c = queue.popleft()
            current_dist = safeness_grid[r][c]

            for dr, dc in directions:
                nr, nc = r + dr, c + dc
                if 0 <= nr < n and 0 <= nc < n and safeness_grid[nr][nc] == -1:
                    safeness_grid[nr][nc] = current_dist + 1
                    queue.append((nr, nc))

        return safeness_grid


class Solution:
    def maximumSafenessFactor(self, grid: List[List[int]]) -> int:
        thieves = []
        dimension = len(grid)
        for i, row in enumerate(grid):
            for j, col in enumerate(grid):
                if grid[i][j] == 1:
                    thieves.append([i,j])
        safe_grid = create_thief_heatmap(thieves, create_grid(dimension))
        if safe_grid[0][0] == 0 or safe_grid[dimension-1][dimension-1] == 0:
            return 0

        directions = [(0, 1), (1, 0), (0, -1), (-1, 0)]
        max_heap = [(-safe_grid[0][0], 0, 0)]
        best_safeness_to_reach = [[-1] * dimension for _ in range(dimension)]
        best_safeness_to_reach[0][0] = safe_grid[0][0]

        while max_heap:
            current_safeness, r, c = heapq.heappop(max_heap)
            current_safeness = -current_safeness
            if r == dimension - 1 and c == dimension - 1:
                return current_safeness
            for dr, dc in directions:
                nr, nc = r + dr, c + dc
                if 0 <= nr < dimension and 0 <= nc < dimension:
                    path_bottleneck = min(current_safeness, safe_grid[nr][nc])
                    if path_bottleneck > best_safeness_to_reach[nr][nc]:
                        best_safeness_to_reach[nr][nc] = path_bottleneck
                        heapq.heappush(max_heap, (-path_bottleneck, nr, nc))
        return 0
if __name__ == "__main__":
    print(Solution().maximumSafenessFactor([[1,0,0],[0,0,0],[0,0,1]]))
    # print(Solution().maximumSafenessFactor([[0,0,1],[0,0,0],[0,0,0]]))
    # print(Solution().maximumSafenessFactor([[0,0,0,1],[0,0,0,0],[0,0,0,0],[1,0,0,0]]))
    # print(Solution().maximumSafenessFactor([[0,1,1],[0,0,1],[1,0,0]]))
    # print(Solution().maximumSafenessFactor([[0,1,1],[0,0,0],[0,1,0]]))
    # print(Solution().maximumSafenessFactor([[0,1,1],[0,1,1],[0,1,1]]))
    # print(Solution().maximumSafenessFactor([[0,1,1],[0,0,0],[0,0,0]]))
    # print(Solution().maximumSafenessFactor([[0,0,0],[0,1,1],[0,0,0]]))
    #print(Solution().maximumSafenessFactor([[0,0,0,0,0,0,0,0,0,0,1,1,1,1,1,1,1,1],[0,0,0,0,0,0,0,0,0,0,0,1,1,1,1,1,1,1],[0,0,0,0,0,0,0,0,0,0,0,0,1,1,1,1,1,1],[0,0,0,0,0,0,0,0,0,0,0,0,0,1,1,1,1,1],[0,0,0,0,0,0,0,0,0,0,0,0,0,0,1,1,1,1],[0,0,0,0,0,0,0,0,0,0,0,0,0,0,1,1,1,1],[0,0,0,0,0,0,0,0,0,0,0,0,0,0,1,1,1,1],[0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,1,1,1],[1,1,0,0,0,0,0,0,0,0,0,0,0,0,0,0,1,1],[1,1,1,0,0,0,0,0,0,0,0,0,0,0,0,0,0,1],[1,1,1,1,0,0,0,0,0,0,0,0,0,0,0,0,0,0],[1,1,1,1,1,0,0,0,0,0,0,0,0,0,0,0,0,0],[1,1,1,1,1,1,0,0,0,0,0,0,0,0,0,0,0,0],[1,1,1,1,1,1,1,0,0,0,0,0,0,0,0,0,0,0],[1,1,1,1,1,1,1,1,0,0,0,0,0,0,0,0,0,0],[1,1,1,1,1,1,1,1,1,0,0,0,0,0,0,0,0,0],[1,1,1,1,1,1,1,1,1,1,0,0,0,0,0,0,0,0],[1,1,1,1,1,1,1,1,1,1,1,0,0,0,0,0,0,0]]))
