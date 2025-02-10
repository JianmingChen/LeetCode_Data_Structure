def candy_maze(candy_map: list[list[int]]) -> int:
    """
    计算在小华先走后，小为能吃到的最大糖果数
    
    Args:
        candy_map: 2行m列的糖果迷宫，每个位置表示糖果数量
        
    Returns:
        int: 小为能吃到的最大糖果数
        
    解题思路：
    1. 首先计算小华的最优路径（使小为能拿到的糖果最少）
    2. 标记小华经过的路径，将这些位置的糖果置为0
    3. 在剩余的糖果中，计算小为能获得的最大糖果数
    """
    if not candy_map or not candy_map[0]:
        return 0
    
    rows, cols = 2, len(candy_map[0])
    
    def find_min_remaining_path(curr_map):
        """
        使用动态规划找到一条路径，使得剩余可获得的最大糖果数最小
        返回路径和对应的最小值
        """
        # dp[i][j] 存储从(i,j)到终点的最小剩余糖果数
        dp = [[float('inf')] * cols for _ in range(rows)]
        # path[i][j] 存储从(i,j)到终点的最优路径的下一步
        path = [[None] * cols for _ in range(rows)]
        
        # 初始化终点
        dp[1][cols-1] = curr_map[1][cols-1]
        
        # 从右到左，从下到上填充dp表
        for j in range(cols-1, -1, -1):
            for i in range(rows-1, -1, -1):
                if i == 1 and j == cols-1:
                    continue
                    
                # 计算向右走的情况
                if j < cols-1:
                    right = dp[i][j+1] + curr_map[i][j]
                    if right < dp[i][j]:
                        dp[i][j] = right
                        path[i][j] = (i, j+1)
                
                # 计算向下走的情况
                if i < rows-1:
                    down = dp[i+1][j] + curr_map[i][j]
                    if down < dp[i][j]:
                        dp[i][j] = down
                        path[i][j] = (i+1, j)
        
        return dp[0][0], path
    
    def mark_path(path, start):
        """标记路径，返回新的糖果地图"""
        new_map = [row[:] for row in candy_map]
        curr = start
        while curr:
            i, j = curr
            new_map[i][j] = 0  # 将路径上的糖果置为0
            if path[i][j]:
                curr = path[i][j]
            else:
                break
        return new_map
    
    def find_max_path(curr_map):
        """找到能获得最大糖果数的路径"""
        dp = [[0] * cols for _ in range(rows)]
        
        # 初始化第一个位置
        dp[0][0] = curr_map[0][0]
        
        # 初始化第一行
        for j in range(1, cols):
            dp[0][j] = dp[0][j-1] + curr_map[0][j]
            
        # 初始化第一列
        for i in range(1, rows):
            dp[i][0] = dp[i-1][0] + curr_map[i][0]
            
        # 填充dp表
        for i in range(1, rows):
            for j in range(1, cols):
                dp[i][j] = max(dp[i-1][j], dp[i][j-1]) + curr_map[i][j]
                
        return dp[1][cols-1]
    
    # 1. 找到小华的最优路径（使剩余可得糖果最小的路径）
    _, first_path = find_min_remaining_path(candy_map)
    
    # 2. 标记小华的路径，创建新的糖果地图
    remaining_map = mark_path(first_path, (0, 0))
    
    # 3. 在剩余糖果中找到小为能获得的最大值
    max_candies = find_max_path(remaining_map)
    
    return max_candies

# 测试代码
def test_candy_maze():
    # 测试用例
    test_cases = [
        # 测试用例1
        [[1, 2, 3],
         [1, 2, 1]],
        # 测试用例2
        [[1, 1, 1],
         [1, 1, 1]],
        # 测试用例3
        [[3, 1, 2, 1],
         [1, 1, 1, 1]]
    ]
    
    for i, case in enumerate(test_cases, 1):
        result = candy_maze(case)
        print(f"测试用例 {i}:")
        print("糖果迷宫:")
        for row in case:
            print(row)
        print(f"小为最多能吃到的糖果数: {result}\n")

if __name__ == "__main__":
    test_candy_maze()
    