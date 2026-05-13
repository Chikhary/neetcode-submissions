class Solution:
    def rotate(self, matrix: List[List[int]]) -> None:
        p1 = 0
        p2 = len(matrix)-1
        while p1<p2:
            for i in range(p2-p1):
                temp = matrix[p1][p1+i]
                matrix[p1][p1+i] = matrix[p2-i][p1]
                matrix[p2-i][p1] = matrix[p2][p2-i]
                matrix[p2][p2-i] = matrix[p1+i][p2]
                matrix[p1+i][p2] = temp
            p1+=1
            p2-=1    
        
                        




        