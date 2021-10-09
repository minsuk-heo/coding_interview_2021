"""
A robot is located at the top-left corner of a m x n grid (marked 'Start' in the diagram below).

The robot can only move either down or right at any point in time. The robot is trying to reach the bottom-right corner of the grid (marked 'Finish' in the diagram below).

How many possible unique paths are there?
Input: m = 3, n = 7
Output: 28

Input: m = 3, n = 2
Output: 3
Explanation:
From the top-left corner, there are a total of 3 ways to reach the bottom-right corner:
1. Right -> Down -> Down
2. Down -> Down -> Right
3. Down -> Right -> Down
"""


def uniquePaths(m: int, n: int) -> int:
    def path(m, n, j, i, dp):
        if i == n - 1 and j == m - 1:
            dp[j][i] = 1
            return dp[j][i]
        if i >= n:
            return 0
        if j >= m:
            return 0
        if dp[j][i] != 0:
            return dp[j][i]
        else:
            dp[j][i] = path(m, n, j + 1, i, dp) + path(m, n, j, i + 1, dp)
            return dp[j][i]

    dp = [[0 for i in range(n)] for j in range(m)]
    path(m, n, 0, 0, dp)
    return dp[0][0]

print(uniquePaths(3,7))