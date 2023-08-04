class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        n = len(nums)
        l = 0
        r = n-1

        arr = [(nums[i], i) for i in range(n)]
        arr.sort(key=lambda x:x[0])

        while l < r:
            sum = arr[l][0] + arr[r][0]
            if sum == target:
                return [arr[l][1],arr[r][1]]
            elif sum < target:
                l = l + 1
            else:
                r = r - 1

        return [-1,-1]