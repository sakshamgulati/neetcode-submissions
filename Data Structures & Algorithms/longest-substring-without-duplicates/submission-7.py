class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        lp,rp= 0,0
        max_count=0
        while rp < len(s): #0< 7
            while s[rp] in s[lp:rp]:
                #do something
                lp+=1
            max_count= max(max_count,rp-lp+1)
            rp+=1
        return max_count
        
        