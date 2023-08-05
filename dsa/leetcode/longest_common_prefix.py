
class Solution:
    def longestCommonPrefix(self, strs: List[str]) -> str:
        n = len(strs)
        root = [{}, n]
        ans_list = []

        for i in range(n):
            temp = root

            m = len(strs[i])
            if m == 0:
                return ""
            for j in range(m):
                c = strs[i][j]
                if (c not in temp[0]):
                    temp[0][c] = [{}, 0]
                temp = temp[0][c]
                temp[1] = temp[1] + 1

        temp = root
        while True:
            keys = list(temp[0].keys())
            keys_len = len(keys)
            if keys_len != 1:
                break
            key = keys[0]
            temp = temp[0][key]
            if temp[1] != n:
                break
            ans_list.append(key)


        return "".join(ans_list)