##############################################################################
# Author: Amit Jaiswal
# LinkedIn: https://www.linkedin.com/in/RonVJ/
# GitHub: https://github.com/RonVJ
# LeetCode: https://leetcode.com/ronvj/

# Problem title: 207. Course Schedule
# Problem link: https://leetcode.com/problems/course-schedule/
# Please reach out to me over LinkedIn if you want to discuss regarding solution
##############################################################################

class Solution:
    def canFinish(self, numCourses: int, prerequisites: List[List[int]]) -> bool:
        incoming_edges = [0] * numCourses
        adj_list = [[] for _ in range(numCourses)]
        n = len(prerequisites)
        for i in range(n):
            incoming_edges[prerequisites[i][0]] = incoming_edges[prerequisites[i][0]] + 1
            adj_list[prerequisites[i][1]].append(prerequisites[i][0])

        pq = deque()
        for i in range(numCourses):
            if incoming_edges[i] == 0:
                pq.append(i)

        num_courses_can_be_taken = 0
        while len(pq) > 0:
            ind = pq.popleft()
            num_courses_can_be_taken = num_courses_can_be_taken + 1
            for nghbr in adj_list[ind]:
                incoming_edges[nghbr] = incoming_edges[nghbr] - 1
                if incoming_edges[nghbr] == 0:
                    pq.append(nghbr)

        if num_courses_can_be_taken == numCourses:
            return True
        return False