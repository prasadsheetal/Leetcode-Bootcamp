def setZeroes(self, matrix: List[List[int]]) -> None:
        """
        Do not return anything, modify matrix in-place instead.
        """
        n=len(matrix)
        m=len(matrix[0])

        rows=[False]*n
        cols=[False]*m

        for i in range(n):
            for j in range(m):

                if matrix[i][j]==0:
                    rows[i]=True
                    cols[j]=True

        for i in range(n):
            for j in range(m):

                if rows[i] or cols[j]:
                    matrix[i][j]=0