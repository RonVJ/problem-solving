##############################################################################
# Author: Amit Jaiswal
# LinkedIn: https://www.linkedin.com/in/RonVJ/
# GitHub: https://github.com/RonVJ
# LeetCode: https://leetcode.com/ronvj/

# Problem title: 1304. Find N Unique Integers Sum up to Zero
# Problem link: https://leetcode.com/problems/find-n-unique-integers-sum-up-to-zero/
# Please reach out to me over LinkedIn if you want to discuss regarding solution
##############################################################################

class Solution:
    def sumZero(self, n: int) -> List[int]:
        ans = []
        for i in range(1, n//2 + 1):
            ans.append(i)
            ans.append(-i)
        if (n & 1) == 1:
            ans.append(0)
        return ans