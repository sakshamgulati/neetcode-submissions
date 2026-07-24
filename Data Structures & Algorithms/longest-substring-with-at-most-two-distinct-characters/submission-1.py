class Solution:
    def lengthOfLongestSubstringTwoDistinct(self, s: str) -> int:
        lp,rp=0,0
        ans=0
        counter= {}
        while rp < len(s):
            counter[s[rp]] = counter.get(s[rp],0)+1
            while len(counter.keys()) > 2:
                counter[s[lp]] -=1
                if counter[s[lp]]==0:
                    counter.pop(s[lp])
                lp+=1
            ans= max(ans,rp-lp+1)
            rp+=1
        return ans
        