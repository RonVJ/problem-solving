##############################################################################
# Author: Amit Jaiswal
# LinkedIn: https://www.linkedin.com/in/RonVJ/
# GitHub: https://github.com/RonVJ
# LeetCode: https://leetcode.com/ronvj/

# Problem title: 435. Non-overlapping Intervals
# Problem link: https://leetcode.com/problems/non-overlapping-intervals/
# Please reach out to me over LinkedIn if you want to discuss regarding solution
##############################################################################

class Solution:
    def eraseOverlapIntervals(self, intervals: List[List[int]]) -> int:
        intervals.sort(key = lambda x: (x[0], x[1]))
        n = len(intervals)

        i = 0
        last_valid_interval_end = -100000
        ans = 0
        while i < n:
            if intervals[i][0] >= last_valid_interval_end:
                last_valid_interval_end = intervals[i][1]
            else:
                ans = ans + 1
                last_valid_interval_end = min(last_valid_interval_end, intervals[i][1])
            i = i + 1
        return ans