class Solution:
    def reverse(self, x: int) -> int:
        ans= 0
        neg_bol = 1 if x >=0 else -1
        x= abs(x)
        while (x / 10) != 0:
            rem = x % 10
            x = x // 10
            ans= ans*10 + rem
        if ans >= -2**31  and ans <= 2**31 -1:
            return ans * neg_bol
        else:
            return 0
