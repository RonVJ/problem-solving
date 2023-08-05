##############################################################################
# Author: Amit Jaiswal
# LinkedIn: https://www.linkedin.com/in/RonVJ/
# GitHub: https://github.com/RonVJ
# LeetCode: https://leetcode.com/ronvj/

# Problem title: 253. Meeting Rooms II
# Problem link: https://leetcode.com/problems/meeting-rooms-ii/
# Please reach out to me over LinkedIn if you want to discuss regarding solution
##############################################################################

class Solution:
    def minMeetingRooms(self, intervals: List[List[int]]) -> int:
        times = []
        for interval in intervals:
            times.append((interval[0], True))
            times.append((interval[1], False))
        times.sort(key=lambda x: (x[0], x[1]))
        print (times)

        count = 0
        max_count = 0
        for time in times:
            if time[1]:
                count = count + 1
            else:
                count = count - 1
            max_count = max(max_count, count)
        return max_count