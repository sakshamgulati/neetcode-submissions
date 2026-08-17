class Solution:
    def isPalindrome(self, s: str) -> bool:
       
        s= [s.lower() for s in s if s.isalnum()]
        lp,rp=0,len(s)-1
        print(s)
        while lp <= rp:
            if s[lp] != s[rp]:
                return False
            lp+=1
            rp-=1
        return True