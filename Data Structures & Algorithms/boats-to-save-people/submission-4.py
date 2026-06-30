class Solution:
    def numRescueBoats(self, people: List[int], limit: int) -> int:
        lp,rp=0,len(people)-1
        count=0
        sorted_p= sorted(people) # 1,2,4,5,lim->10
        while rp >= lp:
            if sorted_p[rp]==limit: 
                count+=1 #2
                rp-=1 #2
            elif sorted_p[lp]==limit:
                count+=1 #1
                lp+=1 #4
            elif sorted_p[lp]+sorted_p[rp]<=limit:
                count+=1
                lp+=1
                rp-=1
            else:
                count+=1
                rp-=1
                
        return count
        
