##############################################################################
# Author: Amit Jaiswal
# LinkedIn: https://www.linkedin.com/in/RonVJ/
# GitHub: https://github.com/RonVJ
# LeetCode: https://leetcode.com/ronvj/

# Problem title: 57. Insert Interval
# Problem link: https://leetcode.com/problems/insert-interval/
# Please reach out to me over LinkedIn if you want to discuss regarding solution
##############################################################################

class Solution:
    def insert(self, intervals: List[List[int]], newInterval: List[int]) -> List[List[int]]:
        n = len(intervals)

        ans = []
        i = 0
        while i < n:
            if intervals[i][1] < newInterval[0]:
                ans.append(intervals[i])
            elif intervals[i][0] > newInterval[1]:
                ans.append(newInterval)
                while i < n:
                    ans.append(intervals[i])
                    i = i + 1
                return ans
            else:
                newInterval[0] = min(newInterval[0], intervals[i][0])
                newInterval[1] = max(newInterval[1], intervals[i][1])
            i = i + 1
        ans.append(newInterval)
        return ans
