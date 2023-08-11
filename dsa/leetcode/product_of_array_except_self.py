##############################################################################
# Author: Amit Jaiswal
# LinkedIn: https://www.linkedin.com/in/RonVJ/
# GitHub: https://github.com/RonVJ
# LeetCode: https://leetcode.com/ronvj/

# Problem title: 238. Product of Array Except Self
# Problem link: https://leetcode.com/problems/jump-game-iii/
# Please reach out to me over LinkedIn if you want to discuss regarding solution
##############################################################################

## Approach 1 - TC: O(n) & SC: O(n) ##
class Solution:
    def productExceptSelf(self, nums: List[int]) -> List[int]:
        n = len(nums)
        prefix_product = [1]*(n + 1)
        suffix_product = [1]*(n + 1)

        ans = []
        for i in range(1, n + 1):
            prefix_product[i] = prefix_product[i - 1] * nums[i - 1]
            suffix_product[n - 1 - i] = suffix_product[n - i] * nums[n - i]

        for i in range(n):
            ans.append(prefix_product[i] * suffix_product[i])
        return ans


## Approach 2 - TC: O(n) & SC: O(1) ##
class Solution:
    def productExceptSelf(self, nums: List[int]) -> List[int]:
        n = len(nums)
        ans = [1] * n

        for i in range(1, n):
            ans[i] = ans[i - 1] * nums[i - 1]

        temp = 1
        for i in range(n - 2, -1, -1):
            temp = temp * nums[i + 1]
            ans[i] = ans[i] * temp
        return ans