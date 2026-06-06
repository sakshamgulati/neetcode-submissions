class Solution:
    def romanToInt(self, s: str) -> int:
        myhash ={
            "I":1,
            "V":5,
            "X":10,
            "L":50,
            "C":100,
            "D":500,
            "M":1000
        }
        #create a FIFO 
        # III
        i= len(s)-1 #2
        rsum= myhash[s[i]]
        i-=1
        while i >= 0: #1>=0
            if myhash[s[i]] < myhash[s[i+1]]: 
                rsum -= myhash[s[i]] #rsum= 
            else:
                rsum += myhash[s[i]]
                
            i-=1 #1
        return rsum

            
        
        