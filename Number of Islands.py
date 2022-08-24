class Solution:
    def numIslands(self, grid: List[List[str]]) -> int:
        self.rows=len(grid)
        self.cols=len(grid[0])
        self.visited=set()
        self.islands=0
        self.grid=grid
        for r in range(self.rows):
            for c in range(self.cols):
                if self.grid[r][c]=="1" and (r,c) not in self.visited:
                    self.bfs(r,c)
                    self.islands+=1
                    
        return self.islands
    def bfs(self,r,c):
        Que=collections.deque()
        self.visited.add((r,c))
        Que.append((r,c))
        while Que:
            r,c=Que.popleft()
            directions=[(-1,0),(1,0),(0,-1),(0,1)]
            for row,col in directions:
                row,col=r+row,c+col
                if row in range(self.rows) and col in range(self.cols) and self.grid[row][col]=="1" and (row,col) not in self.visited:
                    Que.append((row,col))
                    self.visited.add((row,col))