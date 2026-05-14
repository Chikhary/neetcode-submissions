class Solution:
    def hammingWeight(self, n: int) -> int:
        sum1 = 0
        while n>0:
            sum1+=n%2
            n=n//2
        return sum1    