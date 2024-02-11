class Solution:
    def cherryPickup(self, grid: List[List[int]]) -> int:
        ROWS, COLS = len(grid), len(grid[0])
        possible_steps = [-1, 0, 1]
        cache = {}

        def rec(r, c1, c2):
            if (r, c1, c2) in cache:
                return cache[(r, c1, c2)]
            if c1 == c2 or c1 < 0 or c2 < 0 or c1 == COLS or c2 == COLS:
                return 0
            if r == ROWS-1:
                return grid[r][c1] + grid[r][c2]

            res = 0
            for c1_step in possible_steps:
                for c2_step in possible_steps:
                    res =  max(res, rec(r+1, c1+c1_step, c2+c2_step))
            
            cache[(r, c1, c2)] = res + grid[r][c1] + grid[r][c2]
            return cache[(r, c1, c2)]

        return rec(0, 0, COLS-1)