class Solution:
    def romanToInt(self, s: str) -> int:
        dictionary = {
            'I': 1,
            'V': 5,
            'X': 10,
            'L': 50,
            'C': 100,
            'D': 500,
            'M': 1000,
            "IV": 4,
            "IX": 9,
            "XL": 40,
            "XC": 90,
            "CD": 400,
            "CM": 900,
        }
        num = 0
        n = len(s)
        i = 0
        while i < n:
            char = s[i]
            if ((char == 'I') or (char == 'X') or (char == 'C')) and (i < n-1):
                key = "".join([char, s[i+1]])
                if key in dictionary:
                    num = num + dictionary[key]
                    i = i + 2
                    continue
            num = num + dictionary[char]
            i = i + 1
        return num
