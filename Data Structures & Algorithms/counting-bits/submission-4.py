class Solution:
    def countBits(self, n: int) -> List[int]:
        if n==0:
            return [0]
        resultat=[0]
        m=1
        power = 1
        while m<=n:
            if power*2==m:
                resultat.append(1)
                power=m
            else:
                resultat.append(1+resultat[m-power])
            m+=1    
        return resultat            
                       