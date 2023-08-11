from collections import deque

class Solution:

    def updateMatrix(self, mat: List[List[int]]) -> List[List[int]]:
        m = len(mat)
        n = len(mat[0])

        dq = deque()
        inf = 1000000

        for i in range(m):
            for j in range(n):
                if mat[i][j] == 0:
                    dq.append((i, j, 0))
                elif mat[i][j] == 1:
                    mat[i][j] = inf

        while len(dq) != 0:
            r, c, d = dq.popleft()
            if (r - 1 >= 0) and (mat[r-1][c] == inf):
                mat[r-1][c] = d+1
                dq.append((r-1, c, d+1))
            if (r + 1 < m) and (mat[r+1][c] == inf):
                mat[r+1][c] = d+1
                dq.append((r+1, c, d+1))
            if (c - 1 >= 0) and (mat[r][c-1] == inf):
                mat[r][c-1] = d+1
                dq.append((r, c-1, d+1))
            if (c + 1 < n) and (mat[r][c+1] == inf):
                mat[r][c+1] = d+1
                dq.append((r, c+1, d+1))

        return mat
