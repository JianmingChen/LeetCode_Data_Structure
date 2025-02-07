from typing import List

class Solution:
    """
    Problem: Unique Paths II
    
    Given a grid with obstacles, find the number of unique paths from top-left to bottom-right corner.
    - The robot can only move either down or right at any point in time
    - An obstacle and space are marked as 1 and 0 respectively
    - The path sum should avoid obstacles
    
    Constraints:
    - m == obstacleGrid.length
    - n == obstacleGrid[0].length
    - 1 <= m, n <= 100
    - obstacleGrid[i][j] is 0 or 1
    
    Example:
    Input: obstacleGrid = [
        [0,0,0],
        [0,1,0],
        [0,0,0]
    ]
    Output: 2
    Explanation: There are two possible paths:
    1. Right -> Right -> Down -> Down
    2. Down -> Down -> Right -> Right
    The middle cell (1,1) is an obstacle, so we cannot go through it.
    """
    
    def uniquePathsWithObstacles(self, obstacleGrid: List[List[int]]) -> int:
        """
        Solves the unique paths problem using dynamic programming.
        
        Args:
            obstacleGrid (List[List[int]]): m x n grid where 0 is empty and 1 is obstacle
            
        Returns:
            int: Number of unique paths from top-left to bottom-right
            
        Time Complexity: O(m*n) where m,n are dimensions of the grid
        Space Complexity: O(m*n) for the dp array
        
        Dynamic Programming Approach:
        1. Create a dp array where dp[i][j] represents number of unique paths to cell (i,j)
        2. Initialize dp[0][0] based on whether starting cell has obstacle
        3. For each cell (i,j):
           - If cell has obstacle, skip it (paths = 0)
           - Otherwise, paths = paths from above + paths from left
        4. Final answer is in dp[-1][-1]
        """
        m, n = len(obstacleGrid), len(obstacleGrid[0])

        dp = [[0] * n for _ in range(m)]
        

        dp[0][0] = 1 if obstacleGrid[0][0] == 0 else 0

        for i in range(m):
            for j in range(n):
                if obstacleGrid[i][j] == 1:
                    continue
                if i > 0:
                    dp[i][j] += dp[i-1][j]
                    
                if j > 0:
                    dp[i][j] += dp[i][j-1]
                    
        return dp[-1][-1]


# Test case
obstacle_grid = [
    [0,0,0],
    [0,1,0],
    [0,0,0]
]
solution = Solution()
print(f"Input grid:")
for row in obstacle_grid:
    print(row)
print(f"Number of unique paths: {solution.uniquePathsWithObstacles(obstacle_grid)}")  # Expected: 2