class Solution:

    def encode(self, strs: List[str]) -> str:
        res=''
        for items in strs:
            res += str(len(items))+"#"+ items
        return res # 5#Hello5#World


    def decode(self, s: str) -> List[str]:
        i,j=0,0
        ans=[]
        while j < len(s):
            if s[j] == "#":
                lens= int(s[i:j])
                ans.append(s[j+1:j+lens+1])
                i= j+lens+1
                j= i
            j+=1
        return ans
