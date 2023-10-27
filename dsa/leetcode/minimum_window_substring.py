##############################################################################
# Author: Amit Jaiswal
# LinkedIn: https://www.linkedin.com/in/RonVJ/
# GitHub: https://github.com/RonVJ
# LeetCode: https://leetcode.com/ronvj/

# Problem title: 76. Minimum Window Substring
# Problem link: https://leetcode.com/problems/minimum-window-substring/
# Please reach out to me over LinkedIn if you want to discuss regarding solution
##############################################################################

class Solution:
    def minWindow(self, s: str, t: str) -> str:
        hms, hmt = collections.defaultdict(int), collections.defaultdict(int)
        nt = len(t)
        ns = len(s)
        for char in t:
            hmt[char] = hmt[char] + 1

        l = 0
        r = -1
        need = nt
        ans = ns + 1
        count = 0
        ans_l = -1
        ans_r = -1
        while l < ns and r < ns:
            if need > 0:
                r = r + 1
                if r >= ns:
                    break
                char = s[r]
                hms[char] = hms[char] + 1
                if hms[char] <= hmt[char]:
                    need = need - 1
            if need == 0:
                count = r - l + 1
                if count < ans:
                    ans = count
                    ans_l = l
                    ans_r = r
                hms[s[l]] = hms[s[l]] - 1
                if hms[s[l]] < hmt[s[l]]:
                    need = need + 1
                l = l + 1
        if ans_l != -1:
            return s[ans_l: ans_r + 1]
        return ""