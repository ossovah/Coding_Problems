"""
See the problem description at: https://leetcode.com/problems/battleships-in-a-board/
"""class Solution:
    def countBattleships(self, board: List[List[str]]) -> int:
        def find_prev_neighbors(row, col):
            """
            Finds the two previously visited neighbors for each node. One at the the
            same row but at the previous column. The other at the same column but at
            the previous row.
            """
            nei = set()
            if row == 0 and col == 0: return nei
            elif row == 0: 
                nei.add((row, col - 1))
            elif col == 0: 
                nei.add((row - 1, col))
            else:
                nei.add((row, col - 1))
                nei.add((row - 1, col))
        
            return nei
        
        # Count the battleships in the board:
        if not board: return 0
        num_batt = 0            # number of battleships
        rows = len(board)
        cols = len(board[0])
        for r in range(rows):
            for c in range(cols):                
                if board[r][c] == 'X':
                    neighbors = find_prev_neighbors(r, c) # Find previously visited neighbors
                    if not neighbors: # This is applicable to the first row and first column
                        num_batt += 1
                        continue
                    num_batt_nei = 0
                    for nei in neighbors:
                        r_n, c_n = nei
                        if board[r_n][c_n] == 'X':
                            num_batt_nei += 1
                    # If none of the previously visited neighbors were 'X', this is part of a 
                    # new battleship:
                    if num_batt_nei == 0:
                        num_batt += 1
 
        return num_batt