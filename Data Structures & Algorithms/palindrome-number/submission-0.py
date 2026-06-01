class Solution:
    def isPalindrome(self, x: int) -> bool:
        
        int_string= [i for i in str(x)] #("1","2","1")
        lp, rp = 0, len(int_string)-1

        while rp > lp: #1,1
            #check if they are same
            if int_string[lp] != int_string[rp]: #2 != 1
                return False
            rp -=1
            lp +=1
        return True

        

