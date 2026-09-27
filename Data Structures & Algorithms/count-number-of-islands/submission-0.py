class Solution:
            
    def numIslands(self, grid: List[List[str]]) -> int:
        count = 0
        for row in range(len(grid)):
            for col in range(len(grid[0])):
                if grid[row][col] == "1":
                    count += 1
                    sink(grid,row,col)
        return count

directions = [(-1,0),(1,0),(0,-1),(0,1)]
def sink(grid,row,col):
    if row < 0 or row >= len(grid) or col < 0 or col >= len(grid[0]):
        return 
    if grid[row][col] != "1":
        return 
    else:
        grid[row][col] = "0"
        for dr,dc in directions:
            sink(grid,row+dr,col+dc)

        