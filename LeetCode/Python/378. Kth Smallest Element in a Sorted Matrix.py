"""
See the problem description at: https://leetcode.com/problems/kth-smallest-element-in-a-sorted-matrix/

Here are few important notes to the solution:

1) Since both rows and columns are also in increasing order, if k < number of rows, we just need to look into 
the first k rows. Otherwise, we may need to look into all the rows.

2) We also define an array called pointers whose value at index r is the column index of the value 
we are pointing to in row r.

3) We first construct a heap whose size is equal to the number of rows that needs to be considered. We 
populate the heap using the first value in each row and the row index. 

4) We then begin popping values from the heap. Whenever, a value is popped we retrieve its row index. 
Then we look at the correspoinding column index in pointers. If the column doesn't point to the last 
column, we add 1 to the pointer and add the next value to the heap.

5) When the counter is equal to k, we return the last value popped from the heap.

Time complexity: O(min(k, num_rows) + k log(min(k, num_rows)))
Space complexity: O(min(k, num_rows))
"""

class Solution:
    def kthSmallest(self, matrix: List[List[int]], k: int) -> int:
        if not matrix: return 0
        
        num_rows = len(matrix)              # Number of rows
        num_cols = len(matrix[0])           # Number of columns        
        rows2consider = min(num_rows, k)    # Maximum number of row we may need to search to find the k-th value
        pointers = [0] * rows2consider      # Pointers to all those rows
        
        # Construct the initial heap that includes the first element of each row and the row index:
        heap = []
        for r in range(rows2consider):      # r: row index
            heapq.heappush(heap, (matrix[r][0], r))
        
        # Pop the values from the heap. Suppose the popped value is from row r. If the pointer for row r (pointers[r])
        # doesn't point to the last value in the row, add the next value in row r to the heap:
        count = 0
        while True:
            num, r = heapq.heappop(heap)    # r: row index
            count += 1
            if count == k: return num
            if pointers[r] < num_cols - 1:
                pointers[r] += 1
                heapq.heappush(heap, (matrix[r][pointers[r]], r))
