"""
See the problem description at: https://leetcode.com/problems/number-of-islands/
"""
class Solution:
    def numIslands(self, grid: List[List[str]]) -> int:            
        if not grid: return 0
        
        # Store all the edge coordinates in a set called edges:
        edges = set()
        rows = len(grid)
        cols = len(grid[0])
        for i in range(rows):
            for j in range(cols):
                if grid[i][j] == "1":
                    edges.add((i, j))
        """
        Use depth-first search to traverse the graph. All nodes in an island are connected
        and thus every node has at least one neighbor in the island. 
        """
        visited = set()
        islands = 0
        for edge in edges:
            """
            If an edge hasn't been visited yet, neither has any of its "1" neighbors.
            Thus, we can increase the number of islands and use a stack to store and
            visit all the connected nodes in an island:
            """
            if edge not in visited: 
                visited.add(edge)
                islands += 1
                stack = [edge]
                while stack:
                    edge = stack.pop()
                    r, c = edge
                    # Find the neighbors adjacent to edge (r, c):
                    neighbors = [(r+m, c+n) for m in {-1,0,1} for n in {-1, 0, 1} if 0 <= r+m and\
                                  r+m < rows and 0 <= c+n and c+n < cols and abs(m) != abs(n) ]
                    for nei in neighbors:
                        if nei in edges:
                            if nei not in visited:
                                stack.append(nei)
                                visited.add(nei)
        
        return islands