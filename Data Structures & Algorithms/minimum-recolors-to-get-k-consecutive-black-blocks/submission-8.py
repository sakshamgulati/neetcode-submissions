class Solution:
    def minimumRecolors(self, blocks: str, k: int) -> int:
        #sliding indow that goes till the end
        lp,rp=0,k
        mymap={"W":1, "B":0} #WBWBBBW
        ans= 0
        for i in range(rp):
            ans += mymap[blocks[i]]
        iter_ans = ans
        while rp < len(blocks):
            iter_ans = iter_ans + mymap[blocks[rp]] - mymap[blocks[lp]]
            ans= min(iter_ans,ans)
            rp+=1
            lp+=1
        return ans
        