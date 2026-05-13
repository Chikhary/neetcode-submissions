class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        dict1 = {}
        for elem in strs:
            counter = [0]*26
            for letter in elem:
                counter[ord(letter)-ord("a")]+=1
            if tuple(counter) in dict1:
                dict1[tuple(counter)].append(elem)
            else:
                dict1[tuple(counter)] = [elem]
        resultat = []
        for keys in dict1:
            resultat.append(dict1[keys])
        return resultat                    

        