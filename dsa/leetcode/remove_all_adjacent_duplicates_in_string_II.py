from collections import deque


class Solution:
    def removeDuplicates(self, s: str, k: int) -> str:
        dq = deque()

        for char in s:
            if len(dq) == 0:
                dq.append((char, 1))
            else:
                last_char, num_consecutive_duplicates = dq.pop()
                if last_char != char:
                    dq.append((last_char, num_consecutive_duplicates))
                    dq.append((char, 1))
                else:
                    if num_consecutive_duplicates == k - 1:
                        j = k - 2
                        while j > 0:
                            dq.pop()
                            j = j - 1
                    else:
                        dq.append((last_char, num_consecutive_duplicates))
                        dq.append((char, num_consecutive_duplicates + 1))

        return "".join(list(map(lambda x: x[0], list(dq))))
