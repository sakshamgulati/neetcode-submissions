class Solution:
    def numRescueBoats(self, people: List[int], limit: int) -> int:
        #[1,2,3,6,6]
        
        people.sort()
        lp,rp=0,len(people)-1
        ans=0
        while rp >= lp:
            if people[rp]+people[lp] <= limit:
                ans+=1
                lp+=1
                rp-=1
            elif people[rp] <= limit:
                ans+=1
                rp-=1
        return ans
