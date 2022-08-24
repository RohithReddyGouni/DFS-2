class Solution:
    def updateMatrix(self, mat: List[List[int]]) -> List[List[int]]:
        Que=deque()
        m=len(mat)
        n=len(mat[0])
        for i in range(m):
            for j in range(n):
                if mat[i][j]==0:
                    Que.append((i,j))
                else:
                    mat[i][j]=-1;
                    
        count=1
        while Que:
            length=len(Que)
            directions=[(-1,0),(1,0),(0,-1),(0,1)]
            for i in range(length):
                row,col=Que.popleft()
                for nr,nc in directions:
                    nr,nc=row+nr,nc+col
                    if nr in range(m) and nc in range(n) and mat[nr][nc]==-1:
                        mat[nr][nc]=count
                        Que.append((nr,nc))
            count+=1
        return mat