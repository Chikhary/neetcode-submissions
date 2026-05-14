class Solution:
    def countBits(self, n: int) -> List[int]:
        if n==0:
            return [0]
        resultat=[0]
        for i in range(1,n+1):
            j=i
            sum1=0
            while j>0:
                sum1+=j%2
                j=j//2
            resultat.append(sum1)
        return resultat            