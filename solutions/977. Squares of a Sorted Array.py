# Two pointers
# Time: O(n), Space: O(n)
class Solution:
    def sortedSquares(self, nums: List[int]) -> List[int]:
        res = [0] * len(nums)
        l, r = 0, len(nums) - 1
        while l <= r:
            if abs(nums[l]) > abs(nums[r]):
                res[r - l] = nums[l] ** 2
                l += 1
            else:
                res[r - l] = nums[r] ** 2
                r -= 1
        return res

# Time: O(nlogn), Space: O(1)
# Python sorted() solution is O(N) not O(NlogN): https://leetcode.com/problems/squares-of-a-sorted-array/discuss/233054/Python-sorted()-solution-is-O(N)-not-O(NlogN)
class Solution:
    def sortedSquares(self, nums: List[int]) -> List[int]:
        for i in range(len(nums)):
            nums[i] *= nums[i]
        nums.sort()
        return nums
