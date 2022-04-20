# Time: O(n), Space: O(1)
class Solution:
    def findMaxConsecutiveOnes(self, nums: List[int]) -> int:
        res = 0
        cur = 0
        for num in nums:
            if num == 1:
                cur += 1
            else:
                res = max(res, cur)
                cur = 0
        return max(res, cur)
