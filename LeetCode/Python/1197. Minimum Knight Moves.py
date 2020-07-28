"""
See the problem description at: https://leetcode.com/problems/minimum-knight-moves/
"""

class Solution:
    def minKnightMoves(self, x: int, y: int) -> int:
        from collections import deque
        
        if x == 0 and y == 0: return 0
        
        x, y = abs(x), abs(y)        
        queue = collections.deque([(0, 0)]) # x and y coordinates
        moves_to_xy = dict()
        moves_to_xy[0, 0] = 0        
        xy_moves = [(i, j) for i in {-1, 1, 2, -2} for j in {-1, 1, 2, -2} \
                         if abs(i) != abs(j)]        
        
        while queue:
            px, py = queue.popleft()
            n_moves = moves_to_xy[px, py]
            for xm, ym in xy_moves:
                x1, y1 = px + xm, py + ym
                nei = x1, y1
                if nei == (x, y):
                    return n_moves + 1
                xx, yy = nei
                # cond1 = abs(xx) + abs(yy) <= 300 # May not pass the time limit condition
                cond2 = xx <= 300 and xx >= -5 and yy <= 300 and yy >= -5
                if nei not in moves_to_xy and cond2:
                    queue.append(nei)
                    moves_to_xy[nei] = n_moves + 1