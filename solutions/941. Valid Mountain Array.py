# Solution 1 (optimal): One Pointer
# Time: O(n), Space: O(1)

class Solution:
    def validMountainArray(self, arr: List[int]) -> bool:
        i, n = 0, len(arr)
        while (i < n - 1) and (arr[i] < arr[i + 1]):
            i += 1
        if (i == 0) or (i == n - 1):
            return False
        while (i < n - 1) and (arr[i] > arr[i + 1]):
            i += 1
        return i == n - 1


# Solution 2 (optimal): Two Pointers
# Time: O(n), Space: O(1)

class Solution:
    def validMountainArray(self, arr: List[int]) -> bool:
        n = len(arr)
        l, r = 0, len(arr) - 1
        while (l < n - 1) and (arr[l] < arr[l + 1]):
            l += 1
        if l == n - 1:
            return False
        while (r > 0) and (arr[r] < arr[r - 1]):
            r -= 1
        if r == 0:
            return False
        return l == r
