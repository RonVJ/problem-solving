##############################################################################
# Author: Amit Jaiswal
# LinkedIn: https://www.linkedin.com/in/RonVJ/
# GitHub: https://github.com/RonVJ
# LeetCode: https://leetcode.com/ronvj/

# Problem title: 56. Merge Intervals
# Problem link: https://leetcode.com/problems/merge-intervals/
# Please reach out to me over LinkedIn if you want to discuss regarding solution
##############################################################################

class Solution:
    def merge(self, intervals: List[List[int]]) -> List[List[int]]:
        n = len(intervals)
        intervals.sort(key = lambda x: x[0])
        interval_start = intervals[0][0]
        interval_end = intervals[0][1]

        i = 1
        ans = []
        while i < n:
            if intervals[i][0] > interval_end:
                ans.append([interval_start, interval_end])
                interval_start = intervals[i][0]
                interval_end = intervals[i][1]
            else:
                interval_end = max(interval_end, intervals[i][1])
            i = i + 1
        ans.append([interval_start, interval_end])
        return ans