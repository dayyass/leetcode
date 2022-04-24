# Solution 1: optimal
# Time: O(m + n), Space: O(1)
class Solution:
    def merge(self, nums1: List[int], m: int, nums2: List[int], n: int) -> None:
        """
        Do not return anything, modify nums1 in-place instead.
        """
        while (m > 0) and (n > 0):
            if nums1[m-1] > nums2[n-1]:
                nums1[m+n-1] = nums1[m-1]
                m -= 1
            else:
                nums1[m+n-1] = nums2[n-1]
                n -= 1
        while n > 0:
            nums1[n-1] = nums2[n-1]
            n -= 1

# Solution 2: sorting
# Time: O((m+n)log(m+n)), Space: O(1)
class Solution:
    def merge(self, nums1: List[int], m: int, nums2: List[int], n: int) -> None:
        """
        Do not return anything, modify nums1 in-place instead.
        """
        for i in range(len(nums2)):
            nums1[m + i] = nums2[i]
        nums1.sort()  # inplace
