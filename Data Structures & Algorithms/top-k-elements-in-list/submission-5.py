class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        dict1 = {}
        for elem in nums:
            if elem in dict1:
                dict1[elem]+=1
            else:
                dict1[elem]=1
        tab = [[] for i in range(len(nums)+1)]
        for key in dict1:
            tab[dict1[key]].append(key)
        resultat = []
        print(tab)
        for i in range(len(tab)-1,0,-1):
            for elem in tab[i]:
                resultat.append(elem)
                if len(resultat)==k:
                    return resultat                    