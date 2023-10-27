##############################################################################
# Author: Amit Jaiswal
# LinkedIn: https://www.linkedin.com/in/RonVJ/
# GitHub: https://github.com/RonVJ
# LeetCode: https://leetcode.com/ronvj/

# Problem title: 125. Valid Palindrome
# Problem link: https://leetcode.com/problems/valid-palindrome/
# Please reach out to me over LinkedIn if you want to discuss regarding solution
##############################################################################

class Solution:
    def valid_start(self, s, ind):
        n = len(s)
        while ind < n:
            if ((ord(s[ind]) >= 97 and ord(s[ind]) <= 122)
                    or (ord(s[ind]) >= 48 and ord(s[ind]) <= 57)):
                return ind
            ind = ind + 1
        return ind

    def valid_end(self, s, ind):
        while ind >= 0:
            if ((ord(s[ind]) >= 97 and ord(s[ind]) <= 122)
                    or (ord(s[ind]) >= 48 and ord(s[ind]) <= 57)):
                return ind
            ind = ind - 1
        return ind

    def isPalindrome(self, s: str) -> bool:
        n = len(s)
        s = s.lower()
        start = self.valid_start(s, 0)
        end = self.valid_end(s, n - 1)

        while start <= end:
            if s[start] == s[end]:
                start = self.valid_start(s, start + 1)
                end = self.valid_end(s, end - 1)
            else:
                break
        if start < end:
            return False
        return True