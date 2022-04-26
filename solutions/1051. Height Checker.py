# Solution 1 (optimal): Counting Sort
# Time: O(n), Space: O(n)

class Solution:
    def heightChecker(self, heights: List[int]) -> int:
        # <counting sort>
        height2freq = [0] * 101
        for h in heights:
            height2freq[h] += 1
        # </counting sort>
        res = 0
        exp_h = 0
        for h in heights:
            while height2freq[exp_h] == 0:
                exp_h += 1
            if h != exp_h:
                res += 1
            height2freq[exp_h] -= 1
        return res
        

# Solution 2: Sorting
# Time: O(nlogn), Space: O(n)

class Solution:
    def heightChecker(self, heights: List[int]) -> int:
        res = 0
        expected = sorted(heights)
        for i in range(len(heights)):
            if heights[i] != expected[i]:
                res += 1
        return res
