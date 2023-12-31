##############################################################################
# Author: Amit Jaiswal
# LinkedIn: https://www.linkedin.com/in/RonVJ/
# GitHub: https://github.com/RonVJ
# LeetCode: https://leetcode.com/ronvj/

# Problem title: 1. Two Sum
# Problem link: https://leetcode.com/problems/two-sum/
# Please reach out to me over LinkedIn if you want to discuss regarding solution
##############################################################################

class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        n = len(nums)
        l = 0
        r = n-1

        arr = [(nums[i], i) for i in range(n)]
        arr.sort(key=lambda x:x[0])

        while l < r:
            sum = arr[l][0] + arr[r][0]
            if sum == target:
                return [arr[l][1],arr[r][1]]
            elif sum < target:
                l = l + 1
            else:
                r = r - 1

        return [-1,-1]