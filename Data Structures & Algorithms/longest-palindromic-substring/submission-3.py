class Solution:
    def longestPalindrome(self, s: str) -> str:
        n= len(s)
        #if n is odd
        longest=0
        largest_string=""

        for i in range(n):
            
            l,r=i,i
            while l >= 0 and r < n and s[l]==s[r]:
                if r-l+ 1 > longest:
                    longest= r-l+1
                    largest_string = s[l:r+1]
                l = l -1
                r = r + 1
    
        
            l,r=i,i+1
            while l >= 0 and r < n and s[l]==s[r]:
                if r-l+ 1 > longest:
                    longest= r-l+1    
                    largest_string = s[l:r+1]
                l = l -1
                r = r + 1

        return largest_string




                    



