class Solution:
    def lengthOfLastWord(self, s: str) -> int:
        lp,length= len(s)-1, 0
        while s[lp]== " ":
            lp -=1
        while lp >= 0 and s[lp] != " ":
            length +=1
            lp -=1
        return length