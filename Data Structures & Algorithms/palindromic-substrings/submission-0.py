class Solution:
    def countSubstrings(self, s: str) -> int:
        count=0
        ans=[]
        def palindrome(mylist):
            if not mylist: return False
            lp,rp=0,len(mylist)-1
            while rp > lp:
                if mylist[lp]!=mylist[rp]:
                    return False
                rp-=1
                lp+=1
            return True

        for i in range(len(s)):
            ans.append(s[i:i+1])
            for j in range(i+1,len(s)):
                ans.append(s[i:j+1])
        count=[palindrome(i) for i in ans]

        return sum(count)