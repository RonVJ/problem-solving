class Solution:
    def find_if_sums_exist(self, matchsticks, side_len, ind, sum1, sum2, sum3, sum4):
        if ((sum1 > side_len)
                or (sum2 > side_len)
                or (sum3 > side_len)
                or (sum4 > side_len)):
            return False

        if ind == len(matchsticks):
            if ((sum1 != side_len)
                    or (sum2 != side_len)
                    or (sum3 != side_len)
                    or (sum4 != side_len)):
                return False
            return True

        return (self.find_if_sums_exist(matchsticks, side_len, ind+1, sum1 + matchsticks[ind], sum2, sum3, sum4)
                or self.find_if_sums_exist(matchsticks, side_len, ind+1, sum1, sum2 + matchsticks[ind], sum3, sum4)
                or self.find_if_sums_exist(matchsticks, side_len, ind+1, sum1, sum2, sum3 + matchsticks[ind], sum4)
                or self.find_if_sums_exist(matchsticks, side_len, ind+1, sum1, sum2, sum3, sum4 + matchsticks[ind]))

    def makesquare(self, matchsticks: List[int]) -> bool:
        total = sum(matchsticks)
        if total/4 != total//4:
            return False

        side_len = total//4
        matchsticks.sort(reverse=True)
        n = len(matchsticks)
        if matchsticks[0] > side_len:
            return False

        return self.find_if_sums_exist(matchsticks, side_len, 0, 0, 0, 0, 0)