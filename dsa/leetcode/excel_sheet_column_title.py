##############################################################################
# Author: Amit Jaiswal
# LinkedIn: https://www.linkedin.com/in/RonVJ/
# GitHub: https://github.com/RonVJ
# LeetCode: https://leetcode.com/ronvj/

# Problem title: 168. Excel Sheet Column Title
# Problem link: https://leetcode.com/problems/excel-sheet-column-title/
# Please reach out to me over LinkedIn if you want to discuss regarding solution
##############################################################################

# AA- 26
# AB - 27
# AC - 28
# AD - 29
# AE - 30
# 26^3 * (0 ..... 25) + 26^2 * (0 ..... 25) + 26^1 * (0 ..... 25) + (0 .... 25)

class Solution:
    def get_title(self, n, ans_list):
        if n < 0:
            return
        letter = chr((n%26) + 65)
        ans_list.append(letter)
        n = n//26
        self.get_title(n - 1, ans_list)

    def convertToTitle(self, columnNumber: int) -> str:
        ans_list = []
        self.get_title(columnNumber - 1, ans_list)
        ans_list = ans_list[::-1]
        return "".join(ans_list)