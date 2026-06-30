class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        if len(prices) == 1:
            return 0
        
        right = 1
        left = 0
        
        maxprofit = 0

        while right < len(prices):
            maxprofit = max(maxprofit,prices[right] - prices[left])

            if prices[right] < prices[left]:
                left = right
            right +=1




        return maxprofit