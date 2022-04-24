# Solution 1: straightforward
# Time: O(n^2), Space: O(1)
class Solution:
    def checkIfExist(self, arr: List[int]) -> bool:
        for i in range(len(arr)):
            for j in range(i + 1, len(arr)):
                if (2 * arr[i] == arr[j]) or (2 * arr[j] == arr[i]):
                    return True
        return False

# Solution 2: using hash table
# Time: O(n), Space: O(n)
class Solution:
    def checkIfExist(self, arr: List[int]) -> bool:
        hash_set = set()
        for num in arr:
            if (2 * num in hash_set) or ((num % 2 == 0) and (num // 2 in hash_set)):
                return True
            else:
                hash_set.add(num)
        return False
