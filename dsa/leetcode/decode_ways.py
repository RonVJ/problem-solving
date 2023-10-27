##############################################################################
# Author: Amit Jaiswal
# LinkedIn: https://www.linkedin.com/in/RonVJ/
# GitHub: https://github.com/RonVJ
# LeetCode: https://leetcode.com/ronvj/

# Problem title: 91. Decode Ways
# Problem link: https://leetcode.com/problems/decode-ways/
# Please reach out to me over LinkedIn if you want to discuss regarding solution
##############################################################################

class Solution:
    def convert_to_int(self, c):
        return (ord(c) - ord('0'))

    def numDecodings(self, s: str) -> int:
        if s[0] == '0':
            return 0
        n = len(s)
        last_count = 1
        second_last_count = 1
        cur_count = 1

        for i in range(1, n):
            if (self.convert_to_int(s[i]) == 0):
                if (i > 0) and (self.convert_to_int(s[i-1]) == 1 or self.convert_to_int(s[i-1]) == 2):
                    cur_count = second_last_count
                else:
                    return 0
            else:
                cur_count = last_count
                if (self.convert_to_int(s[i-1]) == 1 or (self.convert_to_int(s[i-1]) == 2 and self.convert_to_int(s[i]) <= 6)):
                    cur_count = cur_count + second_last_count
            second_last_count = last_count
            last_count = cur_count
        return cur_count