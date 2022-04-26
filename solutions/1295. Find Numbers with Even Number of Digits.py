# Solution 1: // 10
# Time: O(n), Space: O(1)

class Solution:
    def findNumbers(self, nums: List[int]) -> int:
        res = 0
        for num in nums:

            # count number of digits
            n_digits = 1
            while num // 10 != 0:
                num //= 10
                n_digits += 1

            # check even number of digits
            if n_digits % 2 == 0:
                res += 1

        return res


# Solution 2: log10
# Time: O(n), Space: O(1)

import math
class Solution:
    def findNumbers(self, nums: List[int]) -> int:
        res = 0
        for num in nums:

            # count number of digits
            n_digits = math.floor(math.log10(num)) + 1

            # check even number of digits
            if n_digits % 2 == 0:
                res += 1

        return res


# Solution 3: Use constraints
# Time: O(n), Space: O(1)

class Solution:
    def findNumbers(self, nums: List[int]) -> int:
        res = 0
        for num in nums:
            if (num >= 10 and num <= 99) or (num >= 1000 and num <= 9999) or (num == 100000):
                res += 1
        return res
