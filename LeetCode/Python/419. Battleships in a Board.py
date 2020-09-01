class Solution:
    def countBattleships(self, board: List[List[str]]) -> int:
        """
        Traverse "board" using two for loops. Suppose we encounter 'X' at row r and column s. We check will check
        board[r - 1][c] and board[r][c - 1]. If none is 'X', we will add 1 to the number of battleships. We just
        need to be careful when r = 0 or c = 0.        
        """
        if not board: return 0        
        n_rows = len(board)
        n_cols = len(board[0])
        count = 0
        for r in range(n_rows):
            for c in range(n_cols):
                if board[r][c] == 'X':
                    if r == 0 and c == 0:
                        count += 1
                    elif r == 0:    # i.e., c > 0
                        if board[0][c - 1] != 'X':
                            count += 1
                    elif c == 0:    # i.e., r > 0
                        if board[r - 1][0] != 'X':
                            count += 1
                    else:           # i.e., r,c > 0
                        if board[r][c - 1] != 'X' and board[r - 1][c] != 'X':
                            count += 1
        return count
