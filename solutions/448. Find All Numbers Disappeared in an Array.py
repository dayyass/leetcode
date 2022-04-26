# Time: O(n), Space: O(1)

class Solution:
    def findDisappearedNumbers(self, nums: List[int]) -> List[int]:
        for num in nums:
            idx = abs(num)-1
            if nums[idx] > 0:
                nums[idx] *= -1
        return [i+1 for i, num in enumerate(nums) if num > 0]
