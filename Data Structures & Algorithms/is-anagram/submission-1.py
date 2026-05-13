class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        dict1 = {}
        dict2 = {}
        set1= set()
        set2= set()
        for elem in s:
            set1.add(elem)
            if elem in dict1:
                dict1[elem]+=1
            else:
                dict1[elem]=1
        for elem in t:
            set2.add(elem)
            if elem in dict2:
                dict2[elem]+=1
            else:
                dict2[elem]=1
        if set1!=set2:
            return False        
        for elem in dict1:
            if elem in dict2:
                if dict2[elem]!=dict1[elem]:
                    return False
                else:
                    continue    

            else:
                return False                    
        return True
        