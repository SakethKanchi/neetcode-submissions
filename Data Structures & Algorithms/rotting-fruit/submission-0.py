class Solution:
    def orangesRotting(self, grid: List[List[int]]) -> int:
        minutes = 0
        fresh = 0
        queue = []

        for row in range(len(grid)):
            for col in range(len(grid[0])):
                if grid[row][col] == 1:
                    fresh += 1
                elif grid[row][col] == 2:
                    queue.append((row,col))
        directions = [(-1,0),(1,0),(0,-1),(0,1)]
        while queue and fresh > 0:
            for _ in range(len(queue)):
                row,col = queue.pop(0)
                for dr, dc in directions:
                    nr = row + dr
                    nc = col + dc
                    if nr < 0 or nr >= len(grid) or nc < 0 or nc >= len(grid[0]):
                        continue
                    if grid[nr][nc] != 1:
                        continue
                    grid[nr][nc] = 2
                    fresh -= 1
                    queue.append((nr,nc))
            minutes += 1
        
        return -1 if fresh else minutes