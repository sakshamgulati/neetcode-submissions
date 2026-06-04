class Solution:
    def longestPalindrome(self, s: str) -> str:
        ans=""
        max_count=0
        for i in range(len(s)):
            j,k=i,i
            while j >=0 and k < len(s) and s[j]==s[k]:
                if  (k-j+1)>max_count:
                    max_count= k-j+1
                    ans= s[j:k+1]
                j-=1
                k+=1
        for i in range(len(s)-1):
            j,k=i,i+1
            while j >=0 and k < len(s) and s[j]==s[k]:
                if  (k-j+1)>max_count:
                    max_count= k-j+1
                    ans= s[j:k+1]
                j-=1
                k+=1
        return ans
            





                    



