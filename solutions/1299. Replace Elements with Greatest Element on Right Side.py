# Time: O(n), Space: O(1)
class Solution:
    def replaceElements(self, arr: List[int]) -> List[int]:
        max_val = -1
        for i in range(len(arr) - 1, -1, -1):
            if arr[i] > max_val:
                arr[i], max_val = max_val, arr[i]
            else:
                arr[i] = max_val
        return arr
