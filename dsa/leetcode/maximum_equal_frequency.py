##############################################################################
# Author: Amit Jaiswal
# LinkedIn: https://www.linkedin.com/in/RonVJ/
# GitHub: https://github.com/RonVJ
# LeetCode: https://leetcode.com/ronvj/

# Problem title: 1224. Maximum Equal Frequency
# Problem link: https://leetcode.com/problems/maximum-equal-frequency/
# Please reach out to me over LinkedIn if you want to discuss regarding solution
##############################################################################

class Solution:
    def maxEqualFreq(self, nums: List[int]) -> int:
        n = len(nums)
        frequency = {}
        frequency_of_frequencies = {}

        frequency, frequency_of_frequencies, ans, max_frequency = collections.defaultdict(int), collections.defaultdict(int), 0, 0
        for i in range(n):
            num = nums[i]
            frequency[num] = frequency[num] + 1
            max_frequency = max(max_frequency, frequency[num])
            frequency_of_frequencies[frequency[num]] = frequency_of_frequencies[frequency[num]] + 1
            frequency_of_frequencies[frequency[num]-1] = frequency_of_frequencies[frequency[num]-1] - 1

            if ((max_frequency == 1)
                    or (max_frequency * frequency_of_frequencies[max_frequency] == i)
                    or ((max_frequency-1) * (frequency_of_frequencies[(max_frequency-1)]+1) == i)):
                ans = i + 1
        return ans

