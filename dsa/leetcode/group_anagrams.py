##############################################################################
# Author: Amit Jaiswal
# LinkedIn: https://www.linkedin.com/in/RonVJ/
# GitHub: https://github.com/RonVJ
# LeetCode: https://leetcode.com/ronvj/

# Problem title: 49. Group Anagrams
# Problem link: https://leetcode.com/problems/group-anagrams/
# Please reach out to me over LinkedIn if you want to discuss regarding solution
##############################################################################

class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        n = len(strs)
        hm = {}
        for word in strs:
            sorted_word = "".join(sorted(word))
            if sorted_word not in hm:
                hm[sorted_word] = []
            hm[sorted_word].append(word)

        ans = []
        for sorted_word in hm:
            ans.append(hm[sorted_word])
        return ans