class Solution:
    def missingNumber(self, nums: List[int]) -> int:
        count = 0
        set1 = set(nums)
        for i in range(len(nums)):
            if count in set1:
                count+=1
            else:
                return count    
            
        return count