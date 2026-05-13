class Solution:
    def setZeroes(self, matrix: List[List[int]]) -> None:
        setColumns = set()
        setlignes = set()
        for i in range(len(matrix)):
            for j in range(len(matrix[i])):
                if matrix[i][j]==0:
                    setColumns.add(j)
                    setlignes.add(i)
        for i in range(len(matrix)):
            for j in range(len(matrix[i])):
                if i in setlignes:
                    matrix[i][j] = 0
                if j in setColumns:
                    matrix[i][j] = 0                

        

        
        