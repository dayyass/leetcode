# Solution 1: left/right two pointers (elements to remove are rare)
# Time: O(n), Space: O(1)
class Solution:
    def removeElement(self, nums: List[int], val: int) -> int:
        l, r = 0, len(nums) - 1
        while l <= r:
            if nums[l] == val:
                nums[l] = nums[r]
                r -= 1
            else:
                l += 1
        return l

# Solution 2: slow/fast two pointers (many elements to remove)
# Time: O(n), Space: O(1)
class Solution:
    def removeElement(self, nums: List[int], val: int) -> int:
        i = 0
        for num in nums:
            if num != val:
                nums[i] = num
                i += 1
        return i
