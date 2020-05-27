"""
For the problem description, see: https://leetcode.com/problems/sparse-matrix-multiplication/submissions/
"""
class Solution:
    def multiply(self, A: List[List[int]], B: List[List[int]]) -> List[List[int]]:
        def row_col_mult(row, col):
            """
            This function multiplies row and col and return a scalar. Each element of row and col
            is a tuple containing an index and a value.
            """
            res = 0
            for row_ele in row:
                i, r_val = row_ele
                for col_ele in col:
                    j, c_val = col_ele
                    if i == j:
                        res += r_val * c_val
            return res
        
        # Stroing the non-zero (nz) elements of A's rows in a dictionary:
        A_nz = {}
        for r in range(len(A)):
            row = A[r]
            A_nz[r] = []
            for c in range(len(row)):
                if row[c] != 0:
                    A_nz[r].append((c, row[c]))
        
        # Stroing the non-zero (nz) elements of B's columns in a dictionary:
        B_nz = {}
        for c in range(len(B[0])):
            B_nz[c] = []
            for r in range(len(B)):
                if B[r][c] != 0:
                    B_nz[c].append((r, B[r][c]))
        
        # C = A x B:
        C = []
        for i in range(len(A_nz)):
            C.append([])
            for j in range(len(B_nz)):
                C[i].append(row_col_mult(A_nz[i], B_nz[j]))
                
        return C                            