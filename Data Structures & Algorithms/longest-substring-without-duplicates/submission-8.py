class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        counter= {}
        lp,ans=0,0
        for rp in range(len(s)):
            counter[s[rp]] = counter.get(s[rp],0)+1
            while counter[s[rp]]>1:
                    counter[s[lp]] -=1
                    lp +=1
            ans = max(ans,rp-lp+1)
        return ans

