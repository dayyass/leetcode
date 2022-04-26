# Solution 1 (optimal): When 1 more then 0
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


# Solution 2 (optimal): When 0 more then 1
# Time: O(n), Space: O(1)

class Solution:
    def findMaxConsecutiveOnes(self, nums: List[int]) -> int:
        res = 0
        cur = 0
        for i in nums:
            if i == 1:
                cur += 1
                res = max(res, cur)
            else:
                cur = 0
        return res
