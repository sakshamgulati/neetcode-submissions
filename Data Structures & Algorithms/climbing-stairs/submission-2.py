class Solution:
    def climbStairs(self, n: int) -> int:
        def memoization(n,cache):
            if n <= 2:
                return n
            if n not in cache.keys():
                cache[n]= memoization(n-1,cache)+memoization(n-2,cache)
            
            return cache[n]

        return memoization(n,{})