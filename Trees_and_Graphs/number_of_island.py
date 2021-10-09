"""
Given an m x n 2D binary grid grid which represents a map of '1's (land) and '0's (water), return the number of islands.

An island is surrounded by water and is formed by connecting adjacent lands horizontally or vertically. You may assume all four edges of the grid are all surrounded by water.

Input: grid = [
  ["1","1","1","1","0"],
  ["1","1","0","1","0"],
  ["1","1","0","0","0"],
  ["0","0","0","0","0"]
]
Output: 1

Input: grid = [
  ["1","1","0","0","0"],
  ["1","1","0","0","0"],
  ["0","0","1","0","0"],
  ["0","0","0","1","1"]
]
Output: 3
"""


def numIslands(grid):
    def check_island(i, j, grid):
        west, east, north, south = j - 1, j + 1, i - 1, i + 1
        if west >= 0 and grid[i][west] == "1":
            grid[i][west] = "0"
            check_island(i, west, grid)
        if east < len(grid[i]) and grid[i][east] == "1":
            grid[i][east] = "0"
            check_island(i, east, grid)
        if north >= 0 and grid[north][j] == "1":
            grid[north][j] = "0"
            check_island(north, j, grid)
        if south < len(grid) and grid[south][j] == "1":
            grid[south][j] = "0"
            check_island(south, j, grid)

    m, n = len(grid), len(grid[0])
    cnt = 0
    for i in range(m):
        for j in range(n):
            if grid[i][j] == "1":
                cnt += 1
                check_island(i, j, grid)
    return cnt