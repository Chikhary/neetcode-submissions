class Solution:
    def isValid(self, s: str) -> bool:
        s1= [c for c in s]
        stack = []
        ouvrantes = set(["(","[","{"])
        fermantes = set([")","]","}"])
        
        for i in range(len(s1)):
            char = s1[i]
            if char in ouvrantes:
                stack.append(char)
            elif char in fermantes:
                if stack == []:
                    return False
                ouvrante = stack.pop()
                if ouvrante == "(" and char != ")":
                    return False
                elif ouvrante == "[" and char != "]":
                    return False
                elif ouvrante == "{" and char != "}":
                    return False
                else:
                    continue
        return stack == []                            
            

        