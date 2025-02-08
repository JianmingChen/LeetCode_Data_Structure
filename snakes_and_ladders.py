from typing import List

class Solution:
    """
    Problem: Snakes and Ladders

    You are given an n x n integer matrix board where the cells are labeled from 1 to n^2 in a Boustrophedon style starting from the bottom left of the board (i.e. board[n - 1][0]) and alternating direction each row.

    You start at square 1 of the board. In each move, starting from square curr, do the following:

    Choose a destination square next with a label in the range [curr + 1, min(curr + 6, n^2)].
    This choice simulates the result of a standard 6-sided die roll: i.e., there are always at most 6 destinations, regardless of the size of the board.
    If next has a snake or ladder, you must move to the destination of that snake or ladder. Otherwise, you move to next.
    The game ends when you reach square n^2.
    A board square on row r and column c has a snake or ladder if board[r][c] != -1. The destination of that snake or ladder is board[r][c]. Squares 1 and n^2 do not have snakes or ladders.

    Return the least number of moves required to reach the square n^2, or -1 if it is not possible.
    """
    def snakesAndLadders(self, board: List[List[int]]) -> int:
        """
        Solves the Snakes and Ladders game using BFS to find minimum moves to reach the end.
        
        Args:
            board (List[List[int]]): n x n board where -1 represents empty cell,
                                    positive numbers represent destination of snake/ladder
        
        Returns:
            int: Minimum number of moves to reach the last square, -1 if impossible
        """
        n = len(board)
        # Create cells mapping from 1-based label to 0-based (row, col)
        cells = [None] * (n * n + 1)  # +1 because labels start from 1
        label = 1
        
        # Create mapping from label to board coordinates
        for row in range(n-1, -1, -1):  # Start from bottom row
            # For even rows (from bottom), go left to right
            if (n - 1 - row) % 2 == 0:
                for col in range(n):
                    cells[label] = (row, col)
                    label += 1
            # For odd rows (from bottom), go right to left
            else:
                for col in range(n-1, -1, -1):
                    cells[label] = (row, col)
                    label += 1
        
        # BFS to find shortest path
        dist = {1: 0}  # Distance from start
        queue = [1]    # Start from square 1
        
        while queue:
            curr = queue.pop(0)
            if curr == n * n:  # Reached the end
                return dist[curr]
            
            # Try all possible dice rolls (1-6)
            for next_pos in range(curr + 1, min(curr + 6, n * n) + 1):
                row, col = cells[next_pos]
                # If there's a snake or ladder, update destination
                destination = board[row][col]
                final_pos = next_pos if destination == -1 else destination
                
                # If we haven't visited this position before
                if final_pos not in dist:
                    dist[final_pos] = dist[curr] + 1
                    queue.append(final_pos)
        
        return -1  # Cannot reach the end

# Test case
board = [
    [-1,-1,-1,-1,-1,-1],
    [-1,-1,-1,-1,-1,-1],
    [-1,-1,-1,-1,-1,-1],
    [-1,35,-1,-1,13,-1],
    [-1,-1,-1,-1,-1,-1],
    [-1,15,-1,-1,-1,-1]
]

solution = Solution()
print(f"Minimum moves required: {solution.snakesAndLadders(board)}")