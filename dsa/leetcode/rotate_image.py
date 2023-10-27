##############################################################################
# Author: Amit Jaiswal
# LinkedIn: https://www.linkedin.com/in/RonVJ/
# GitHub: https://github.com/RonVJ
# LeetCode: https://leetcode.com/ronvj/

# Problem title: 48. Rotate Image
# Problem link: https://leetcode.com/problems/rotate-image/
# Please reach out to me over LinkedIn if you want to discuss regarding solution
##############################################################################

class Solution:
    def rotate_matrix(self, matrix, n, base_x, base_y):
        if n < 2:
            return

        for k in range(n-1):
            changes = [[(n-1-k), -k], [k, (n-1-k)], [-(n-1-k), k], [-k, -(n-1-k)]]
            nc = len(changes)

            cur_x = base_x
            cur_y = base_y + k
            temp = matrix[cur_x][cur_y]
            for i in range(nc-1):
                next_x = cur_x + changes[i][0]
                next_y = cur_y + changes[i][1]
                matrix[cur_x][cur_y] = matrix[next_x][next_y]
                cur_x = next_x
                cur_y = next_y
            matrix[cur_x][cur_y] = temp
        self.rotate_matrix(matrix, n-2, base_x+1, base_y+1)

    def rotate(self, matrix: List[List[int]]) -> None:
        """
        Do not return anything, modify matrix in-place instead.
        """
        self.rotate_matrix(matrix, len(matrix), 0, 0)
