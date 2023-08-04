import queue

class Solution:
    def longestDiverseString(self, a: int, b: int, c: int) -> str:
        pq = queue.PriorityQueue()
        a = -a
        b = -b
        c = -c
        pq.put((a, 'a'))
        pq.put((b, 'b'))
        pq.put((c, 'c'))

        ans = ""
        while not pq.empty():
            count, char = pq.get()
            if count == 0:
                continue
            n = len(ans)
            if (n >= 2) and ((ans[n-1] == char) and (ans[n-2] == char)):
                next_count, next_char = pq.get()
                if next_count != 0:
                    ans = "".join([ans, next_char])
                    pq.put((next_count+1, next_char))
                    pq.put((count, char))
                else:
                    return ans

            else:
                ans = "".join([ans, char])
                pq.put((count+1, char))
        return ans


