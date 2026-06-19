class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        fp,sp=0,1
        profit=0
        while sp < len(prices):
            if prices[sp] < prices[fp]:
                fp= sp
            else:
                profit = max(prices[sp]-prices[fp],profit)
            sp+=1
        return profit