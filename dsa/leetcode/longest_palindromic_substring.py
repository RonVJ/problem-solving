class Solution:
    def longestPalindrome(self, s: str) -> str:
        n = len(s)
        max_count = 0
        ans = ""

        def get_count(j, k, count):
            while (j >= 0) and (k < n):
                if (s[j] != s[k]):
                    break
                count = count + 2
                j = j - 1
                k = k + 1
            return count, j, k

        for i in range(n):
            count, j, k = get_count(i-1, i+1, 1)
            if count > max_count:
                max_count = count
                ans = s[j+1:k]

            count, j, k = get_count(i, i+1, 0)
            if count > max_count:
                max_count = count
                ans = s[j+1:k]

        return ans