"""
See the problem description at: https://leetcode.com/problems/toeplitz-matrix/
"""

class Solution:
    def isToeplitzMatrix(self, matrix: List[List[int]]) -> bool:
        """
        All the elements that must be equal can be considered to belong to the same
        group. The first elements in the groups are the elements in the first row as
        well as the first elements in the first column. Suppose the first element in
        a group is located in position (0, c). The next element would be (1, c+1)...
        Thus, we can obtain the elements in each group and check if they are all the
        same as the first element in the group.        
        """
        def valid(num, i, j, matrix, rows, cols):
            """
            This function determines if all the elements in a group are equal to the 
            first element in the group.
            """
            row = i + 1 
            col = j + 1
            
            # Check if any of the elements in a certain group is invalid:
            while row < rows and col < cols:
                if matrix[row][col] != num: return False
                row += 1
                col += 1
            
            # Otherwise, the group is valid, thus:
            return True
        
        if not matrix: return False
        rows = len(matrix)
        cols = len(matrix[0])
        
        # Check if any of the groups corresponding to the elements of the first row is invalid:
        for c in range(cols):
            if not valid(matrix[0][c], 0, c, matrix, rows, cols): return False
        
        # Check if any of the groups corresponding to the elements of the first column is invalid:
        for r in range(1, rows):
            if not valid(matrix[r][0], r, 0, matrix, rows, cols): return False

        # Otherwise, all groups are valid and thus:
        return True               