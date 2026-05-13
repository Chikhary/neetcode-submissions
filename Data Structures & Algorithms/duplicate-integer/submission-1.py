class Solution:
    def hasDuplicate(self, nums: List[int]) -> bool:
        set1 = set()
        for elem in nums:
            if elem in set1:
                return True
            set1.add(elem)
        return False       
        