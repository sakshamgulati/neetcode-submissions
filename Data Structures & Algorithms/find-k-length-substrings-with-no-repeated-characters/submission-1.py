class Solution:
    def numKLenSubstrNoRepeats(self, s: str, k: int) -> int:
        #abcdeeffgh, 3
        lp, rp =0,0
        ans=0
        while rp < len(s):
            if rp-lp+1 == k:
                if len(set(s[lp:rp+1]))==len(s[lp:rp+1]):
                    ans+=1
                    lp+=1
                else:
                    while len(set(s[lp:rp+1]))!=len(s[lp:rp+1]):
                        lp+=1
            rp+=1
        return ans