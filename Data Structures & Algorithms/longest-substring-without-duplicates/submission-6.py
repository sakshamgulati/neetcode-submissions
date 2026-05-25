class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        lp,rp=0,0
        max_len= 0
        while rp < len(s):
            while rp-lp+1 != len(set(s[lp:rp+1])):
                lp +=1
            max_len= max(max_len,rp-lp+1)
            rp+=1
        return max_len
        