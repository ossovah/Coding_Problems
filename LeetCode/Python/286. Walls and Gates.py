"""
See the problem description at: https://leetcode.com/problems/walls-and-gates/
"""
class Solution:
    def wallsAndGates(self, rooms: List[List[int]]) -> None:
        """
        Do not return anything, modify rooms in-place instead.
        """
        def find_neighbors(r, c, rows, cols):
            """
            Finds the neighbors list for every (r,c) coordinate in a grid with the
            number of rows equal to rows and the number of columns equal to cols
            """
            return [(r + m, c + n) for m in [-1, 0, 1] for n in [-1, 0, 1] if 0 <= r + m \
                    and r + m < rows and 0 <= c + n and c + n < cols and abs(m) != abs(n)]
        
        if not rooms: return rooms
        
        rows = len(rooms)
        cols = len(rooms[0])        
        queue = collections.deque([])
        
        """
        Use breadth-first search (BFS) to traverse the graph. We begin from the gates and in
        every step, we only visit the neighbors of the first node in the queue (as done in BFS).
        If a neighbor has not been reached yet (which can be found out by looking at its value),
        we will add it to the queue. 
        BFS ensures that every visited node is approach by its closest gate first.
        """
        for r in range(rows):
            for c in range(cols):
                if rooms[r][c] == 0:
                    queue.append((r, c))
        while queue:
            r, c = queue.popleft()
            val = rooms[r][c]
            neighbors = find_neighbors(r, c, rows, cols)
            for nei in neighbors:
                i, j = nei
                if rooms[i][j] == 2147483647:
                    rooms[i][j] = val + 1
                    queue.append(nei)