##############################################################################
# Author: Amit Jaiswal
# LinkedIn: https://www.linkedin.com/in/RonVJ/
# GitHub: https://github.com/RonVJ
# LeetCode: https://leetcode.com/ronvj/

# Problem title: 54. Spiral Matrix
# Problem link: https://leetcode.com/problems/spiral-matrix/
# Please reach out to me over LinkedIn if you want to discuss regarding solution
##############################################################################

class Solution:
    def spiralOrder(self, matrix: List[List[int]]) -> List[int]:
        m = len(matrix)
        n = len(matrix[0])

        operations = [(0, 1), (1, 0), (0, -1), (-1, 0)]
        num_times_perform_operation = [n, m-1]
        current_operation = 0

        cur_x = 0
        cur_y = -1
        ans = []
        numbers_covered = 0
        total_numbers_to_be_covered = m * n
        while numbers_covered < total_numbers_to_be_covered:
            num_times_performed = 0
            while num_times_performed < num_times_perform_operation[current_operation%2]:
                cur_x = cur_x + operations[current_operation][0]
                cur_y = cur_y + operations[current_operation][1]
                ans.append(matrix[cur_x][cur_y])
                numbers_covered = numbers_covered + 1
                num_times_performed = num_times_performed + 1
            num_times_perform_operation[current_operation%2] = num_times_perform_operation[current_operation%2] - 1
            current_operation = (current_operation + 1)%4
        return ans