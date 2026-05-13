class Solution:
    def spiralOrder(self, matrix: List[List[int]]) -> List[int]:
        top = 0
        bottom = len(matrix)-1
        right = len(matrix[0])-1
        left = 0  
        resultat=[]
        while top<=bottom and left<=right:
            #ligne 1
            for i in range(left,right+1):
                resultat.append(matrix[top][i])
            top+=1
            #ligne 2
            for i in range(top,bottom+1):
                resultat.append(matrix[i][right])
            #ligne 3
            right-=1
            if top<=bottom:
                for i in range(right,left,-1):
                    resultat.append(matrix[bottom][i])
            #ligne 4
            if left<=right:
                bottom-=1
                for i in range(bottom+1,top-1,-1):
                    resultat.append(matrix[i][left])
            left+=1                
            
        return resultat            


        