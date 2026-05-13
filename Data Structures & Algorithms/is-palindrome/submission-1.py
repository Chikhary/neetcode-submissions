class Solution:
    def isPalindrome(self, s: str) -> bool:
        s1 = s.replace(" ","")
        s1 = s1.lower()
        s1 = "".join(c for c in s1 if c.isalpha() or c.isdigit())
        print(s1)    
        return s1==s1[::-1]    