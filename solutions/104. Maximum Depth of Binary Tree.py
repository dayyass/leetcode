# Solution 1: "Top-down"
# Time: O(n), Space: O(n)

class Solution:
    def maxDepth(self, root: Optional[TreeNode]) -> int:
        return self.helper(root, 1)
        
    def helper(self, node, val):
        if not node:
            return val - 1
        left_depth = self.helper(node.left, val + 1)
        right_depth = self.helper(node.right, val + 1)
        return max(left_depth, right_depth)


# Solution 2: "Bottom-up"
# Time: O(n), Space: O(n)

class Solution:
    def maxDepth(self, root: Optional[TreeNode]) -> int:
        if not root:
            return 0
        left = self.maxDepth(root.left)
        right = self.maxDepth(root.right)
        return 1 + max(left, right)
