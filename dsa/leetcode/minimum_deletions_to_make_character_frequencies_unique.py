class Solution:
    def minDeletions(self, s: str) -> int:
        frequency_map = {}
        for char in s:
            if char not in frequency_map:
                frequency_map[char] = 0
            frequency_map[char] = frequency_map[char] + 1

        values = list(frequency_map.values())
        values.sort()
        m = len(values)

        ans = 0
        for i in range(m-1, 0, -1):
            if values[i-1] >= values[i]:
                ans = ans + (values[i-1] - max(0, (values[i] - 1)))
                values[i-1] = max(0, (values[i] - 1))

        return ans