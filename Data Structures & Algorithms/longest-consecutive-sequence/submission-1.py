class Solution:
    def longestConsecutive(self, nums: List[int]) -> int:
        set1 = set(nums)
        set2 = set()
        longuest = 0
        for i in range(len(nums)):
            current = nums[i]
            if (current -1) not in set1:
                longSeq = 1
                set2.add(current)
                while (current+1) in set1:
                    longSeq+=1
                    current+=1
                    set2.add(current)
                longuest = max(longuest,longSeq)    
            if current in set2:
                continue
        return longuest        




                       
                



        