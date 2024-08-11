# https://leetcode.com/problems/regions-cut-by-slashes

class Solution:
    def regionsBySlashes(self, grid: List[str]) -> int:
        n = len(grid)
        expanded_grid = [[0] * (3 * n) for i in range(3 * n)]
        
        for i in range(n):
            for j in range(n):
                if grid[i][j] == '/':
                    expanded_grid[3 * i][3 * j + 2] = 1
                    expanded_grid[3 * i + 1][3 * j + 1] = 1
                    expanded_grid[3 * i + 2][3 * j] = 1
                elif grid[i][j] == '\\':
                    expanded_grid[3 * i][3 * j] = 1
                    expanded_grid[3 * i + 1][3 * j + 1] = 1
                    expanded_grid[3 * i + 2][3 * j + 2] = 1

        def dfs(x, y):
            if 0 <= x < 3 * n and 0 <= y < 3 * n and expanded_grid[x][y] == 0:
                expanded_grid[x][y] = 1
                dfs(x + 1, y)
                dfs(x - 1, y)
                dfs(x, y + 1)
                dfs(x, y - 1)
        
        regions = 0
        for i in range(3 * n):
            for j in range(3 * n):
                if expanded_grid[i][j] == 0:
                    dfs(i, j)
                    regions += 1
                    
        return regions
