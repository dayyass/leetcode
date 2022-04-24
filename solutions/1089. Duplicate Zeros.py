# Time: O(n^2), Space: O(1)
class Solution:
    def duplicateZeros(self, arr: List[int]) -> None:
        """
        Do not return anything, modify arr in-place instead.
        """
        i, n = 0, len(arr)
        while i < n:
            if arr[i] == 0:
                for j in range(n - 2, i - 1, -1):
                    arr[j+1] = arr[j]
                i += 1
            i += 1


# TODO:
# Time: O(n), Space: O(1)
