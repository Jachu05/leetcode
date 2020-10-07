from typing import List


class Solution:
    def uniquePathsIII(self, grid: List[List[int]]) -> int:
        cache = set()

        seen = [[0 for _ in range(len(grid[0]))] for _ in range(len(grid))]

        def check_i_j_in_grid(i, j):
            if 0 <= i <= len(grid) and 0 <= j <= len(grid[0]):
                return True
            else:
                return False

        def check_if_all_field_marked(grid):
            for row in grid:
                if 0 in row:
                    return False

        def trav(i, j, path):
            if check_i_j_in_grid(i, j):
                return

            if grid[i][j] == 1 or grid[i][j] == -1:
                return

            if grid[i][j] == 2:
                if check_if_all_field_marked(grid):
                    cache.add(path)
                    return

            trav(i - 1, j, path + [(i, j)])
            trav(i + 1, j, path + [(i, j)])
            trav(i, j - 1, path + [(i, j)])
            trav(i, j + 1, path + [(i, j)])

        trav(0, 0, [])
        #try to add to cache in reverse way, paths to current i,j
        return cache


print(Solution().uniquePathsIII(grid=[[1, 0, 0], [0, 0, 0], [0, 0, 2]]))
# print(Solution().uniquePathsIII(grid=[[1, 0, 0, 0], [0, 0, 0, 0], [0, 0, 2, -1]]))
# print(Solution().uniquePathsIII(grid=[[1, 0, 0, 0], [0, 0, 0, 0], [0, 0, 0, 2]]))
