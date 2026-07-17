class Solution:
    def appendCharacters(self, s: str, t: str) -> int:
       
        i,j= 0,0
        while i < len(s) and j < len(t): #s =rabbbit, t= rabbit
            if s[i] != t[j]:
                i+=1
            else:
                i+=1
                j+=1
        return len(t)-j
