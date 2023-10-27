##############################################################################
# Author: Amit Jaiswal
# LinkedIn: https://www.linkedin.com/in/RonVJ/
# GitHub: https://github.com/RonVJ
# LeetCode: https://leetcode.com/ronvj/

# Problem title: 252. Meeting Rooms
# Problem link: https://leetcode.com/problems/meeting-rooms/
# Please reach out to me over LinkedIn if you want to discuss regarding solution
##############################################################################

class Solution:
    def canAttendMeetings(self, intervals: List[List[int]]) -> bool:
        n = len(intervals)
        intervals.sort(key=lambda x: x[0])

        i = 0
        last_meeting_end_time = -1
        while i < n:
            if intervals[i][0] < last_meeting_end_time:
                break
            last_meeting_end_time = intervals[i][1]
            i = i + 1

        if i == n:
            return True
        return False