# Solution 1: Recursive
# Time: O(n), Space: O(n)

class Solution:
    def isSymmetric(self, root: Optional[TreeNode]) -> bool:
        return self.compare(root.left, root.right)
    
    def compare(self, left, right):
        if not left and not right:
            return True
        if not left or not right:
            return False
        if left.val != right.val:
            return False
        out_pair = self.compare(left.left, right.right)
        in_pair = self.compare(left.right, right.left)
        return out_pair and in_pair


# Solution 2: Iterative
# Time: O(n), Space: O(n)

class Solution:
    def isSymmetric(self, root: Optional[TreeNode]) -> bool:
        stack = [(root.left, root.right)]
        while stack:
            left, right = stack.pop()
            if not left and not right:
                continue
            if not left or not right:
                return False
            if left.val != right.val:
                return False
            stack.append((left.left, right.right))
            stack.append((left.right, right.left))
        return True
