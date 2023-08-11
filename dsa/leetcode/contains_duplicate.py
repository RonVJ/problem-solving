##############################################################################
# Author: Amit Jaiswal
# LinkedIn: https://www.linkedin.com/in/RonVJ/
# GitHub: https://github.com/RonVJ
# LeetCode: https://leetcode.com/ronvj/

# Problem title: 217. Contains Duplicate
# Problem link: https://leetcode.com/problems/contains-duplicate/
# Please reach out to me over LinkedIn if you want to discuss regarding solution
##############################################################################

class Solution:
    def containsDuplicate(self, nums: List[int]) -> bool:
        contains = set()
        for num in nums:
            if num in contains:
                return True
            contains.add(num)
        return False