# Solution 1: Recursive
# Time: O(n), Space: O(n)

class Solution:
    def preorderTraversal(self, root: Optional[TreeNode]) -> List[int]:
        res = []
        self.helper(root, res)
        return res
    
    def helper(self, node, res):
        if node:
            res.append(node.val)
            self.helper(node.left, res)
            self.helper(node.right, res)


# Solution 2: Iterative
# Time: O(n), Space: O(n)

class Solution:
    def preorderTraversal(self, root: Optional[TreeNode]) -> List[int]:
        res = []
        stack = [root]
        while stack:
            node = stack.pop()
            if node:
                res.append(node.val)
                stack.append(node.right)
                stack.append(node.left)
        return res


# All DFS traversals:
# https://leetcode.com/explore/learn/card/data-structure-tree/134/traverse-a-tree/929/discuss/283746/All-DFS-traversals-(preorder-inorder-postorder)-in-Python-in-1-line

class Solution:
    def preorderTraversal(self, root: Optional[TreeNode]) -> List[int]:
        return [root.val] + self.preorderTraversal(root.left) + self.preorderTraversal(root.right) if root else []


# TODO:
# Add optimal Morris Traversal
