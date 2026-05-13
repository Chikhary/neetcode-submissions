class Solution:
    def threeSum(self, nums: List[int]) -> List[List[int]]:
        nums2 = sorted(nums)
        resultat = []
        for i in range(len(nums2)-2):
            elem1 = nums2[i]
            j=i+1
            k = len(nums2)-1
            while j<k:
                if nums2[j]+nums2[k]+elem1<0:
                    j+=1
                elif nums2[j]+nums2[k]+elem1>0:
                    k-=1
                elif nums2[j]+nums2[k]+elem1==0:
                    temp = [nums2[i],nums2[j],nums2[k]]
                    if temp not in resultat:
                        resultat.append([nums2[i],nums2[j],nums2[k]])
                    j+=1
                    
        return resultat            


        