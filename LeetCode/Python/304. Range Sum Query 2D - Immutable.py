"""
See the problem description at: https://leetcode.com/problems/range-sum-query-2d-immutable/
"""

class NumMatrix:
    """
    The following solution computes the cumulative sum of the 2D grid from the origin to every point in 
    the grid and it does so in the __init__ function. Then for any quey, we just need to compute a simple
    equation. Does the time complexity is O(1) and the space complexity is O(MN). This approach is similar
    to Approach 4 in https://leetcode.com/articles/range-sum-query-2d-immutable/
    """
    def __init__(self, matrix: List[List[int]]):
        self.matrix = matrix
        self.sum_dk = dict()
        n_rows = len(self.matrix)
        if n_rows:
            n_cols = len(self.matrix[0])
            for r in range(-1, n_rows):
                for c in range(-1, n_cols):
                    if r == -1 or c == -1:
                        self.sum_dk[r, c] = 0
                    elif r == 0:
                        self.sum_dk[0, c] = self.matrix[0][c] if c == 0 else self.matrix[0][c] \
                        + self.sum_dk[0, c-1]
                    elif c == 0:
                        self.sum_dk[r, 0] = self.matrix[r][0] + self.sum_dk[r-1, 0]
                    else:
                            self.sum_dk[r, c] = self.matrix[r][c] + self.sum_dk[r-1, c] + self.sum_dk[r, c-1] \
                        - self.sum_dk[r-1, c-1]

    def sumRegion(self, row1: int, col1: int, row2: int, col2: int) -> int:
        
        n_rows = len(self.matrix)
        if not n_rows: return 0
        
        return self.sum_dk[row2, col2] - self.sum_dk[row1-1, col2] - self.sum_dk[row2, col1-1] \
    + self.sum_dk[row1-1, col1-1]