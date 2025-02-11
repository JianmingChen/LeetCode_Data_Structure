def count_bst(n: int, k: int) -> int:
    """
    计算节点数为n，高度不超过k的不同二叉查找树的个数
    
    Args:
        n: 节点个数 (1到n的数字构成二叉查找树)
        k: 最大高度限制
        
    Returns:
        int: 满足条件的二叉查找树个数
        
    动态规划思路：
    dp[i][j][h] 表示使用1到i中的j个数，构造高度为h的二叉查找树的个数
    """
    if n == 0 or k == 0:
        return 0
        
    # dp[i][j][h]: 使用前i个数中的j个数构造高度为h的BST的个数
    dp = [[[0] * (k + 1) for _ in range(n + 1)] for _ in range(n + 1)]
    
    # 初始化：一个节点的树，高度为1
    for i in range(1, n + 1):
        dp[i][1][1] = i
    
    # 填充dp数组
    for i in range(1, n + 1):  # 可用的最大数
        for j in range(2, i + 1):  # 使用的节点数
            for h in range(2, k + 1):  # 当前高度
                # 枚举根节点
                for root in range(1, i + 1):
                    # 左子树可用的数的个数
                    left_count = root - 1
                    # 右子树可用的数的个数
                    right_count = i - root
                    
                    # 枚举左子树使用的节点数
                    for left_nodes in range(0, min(left_count + 1, j)):
                        right_nodes = j - 1 - left_nodes
                        if right_nodes > right_count:
                            continue
                            
                        # 枚举左右子树的高度
                        for left_height in range(0, h):
                            for right_height in range(0, h):
                                # 确保至少有一个子树的高度为h-1
                                if max(left_height, right_height) != h - 1:
                                    continue
                                    
                                # 计算左子树的方案数
                                left_ways = dp[root-1][left_nodes][left_height] if left_nodes > 0 else 1
                                
                                # 计算右子树的方案数
                                right_ways = dp[i-root][right_nodes][right_height] if right_nodes > 0 else 1
                                
                                dp[i][j][h] += left_ways * right_ways
    
    # 统计所有高度不超过k的方案数
    total = 0
    for h in range(1, k + 1):
        total += dp[n][n][h]
    
    return total

def main():
    """
    处理输入并输出结果
    """
    try:
        # 读取输入
        n, k = map(int, input().strip().split())
        
        # 检查输入范围
        if not (0 < n < 36 and 0 < k < 36):
            raise ValueError("Input out of range")
            
        # 计算结果
        result = count_bst(n, k)
        
        # 输出结果
        print(result)
        
    except Exception as e:
        print(f"Error: {e}")

if __name__ == "__main__":
    main()
