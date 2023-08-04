class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        dictionary = {}
        n = len(s)
        l = 0
        max_len = 0
        for i in range(n):
            char = s[i]
            if (char in dictionary) and dictionary[char] >= l:
                l = dictionary[char]+1
            dictionary[char] = i
            substr_len = i - l + 1
            max_len = max(max_len, substr_len)
        return max_len