class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        dict2 = {}
        for i in range(len(nums)):
            if target - nums[i] in dict2:
                return [dict2[target - nums[i]],i]
            dict2[nums[i]] = i        
        