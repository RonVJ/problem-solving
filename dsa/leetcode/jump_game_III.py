##############################################################################
# Author: Amit Jaiswal
# LinkedIn: https://www.linkedin.com/in/RonVJ/
# GitHub: https://github.com/RonVJ
# LeetCode: https://leetcode.com/ronvj/

# Problem title: 1306. Jump Game III
# Problem link: https://leetcode.com/problems/jump-game-iii/
# Please reach out to me over LinkedIn if you want to discuss regarding solution
##############################################################################

class Solution:
    def dfs(self, arr, ind, visited):
        n = len(arr)
        if (ind < 0) or (ind >= n) or (visited[ind]):
            return False
        if arr[ind] == 0:
            return True
        visited[ind] = True
        if self.dfs(arr, ind + arr[ind], visited):
            return True
        return self.dfs(arr, ind - arr[ind], visited)

    def canReach(self, arr: List[int], start: int) -> bool:
        n = len(arr)
        visited = [False for i in range(n)]
        return self.dfs(arr, start, visited)