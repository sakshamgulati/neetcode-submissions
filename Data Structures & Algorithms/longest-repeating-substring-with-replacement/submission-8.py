class Solution:
    def characterReplacement(self, s: str, k: int) -> int:
        lp,ans=0,0
        counter={}
        for rp in range(len(s)):
            #add to the counter
            counter[s[rp]]= counter.get(s[rp],0)+1
            #find the most frequent element
            maxFreq = sorted(counter.values(), reverse= True)[0]
            
            while maxFreq + k < rp - lp +1 :
                counter[s[lp]] -=1
                lp +=1
            ans= max(ans,rp-lp+1)

        return ans