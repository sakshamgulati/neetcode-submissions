class Solution:
    def validPalindrome(self, s: str) -> bool:
        fp,sp=0,len(s)-1
        def check_palindrome(fp,sp):
            while sp > fp:
                if s[sp]!=s[fp]:
                    return False
                sp-=1
                fp+=1
            return True
        
        while sp > fp:
            if s[fp] != s[sp]:
                return check_palindrome(fp+1,sp) or check_palindrome(fp,sp-1)
            sp-=1
            fp+=1
        return True

        