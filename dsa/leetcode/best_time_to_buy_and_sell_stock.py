##############################################################################
# Author: Amit Jaiswal
# LinkedIn: https://www.linkedin.com/in/RonVJ/
# GitHub: https://github.com/RonVJ
# LeetCode: https://leetcode.com/ronvj/

# Problem title: 121. Best Time to Buy and Sell Stock
# Problem link: https://leetcode.com/problems/best-time-to-buy-and-sell-stock/
# Please reach out to me over LinkedIn if you want to discuss regarding solution
##############################################################################

class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        min_price = prices[0]
        n = len(prices)
        max_profit = 0
        for i in range(1, n):
            profit = prices[i] - min_price
            min_price = min(min_price, prices[i])
            max_profit = max(max_profit, profit)
        return max_profit