# Solution 1: Recursive
# Time: O(n), Space: O(n)

class Solution:
    def inorderTraversal(self, root: Optional[TreeNode]) -> List[int]:
        res = []
        self.helper(root, res)
        return res
    
    def helper(self, node, res):
        if node:
            self.helper(node.left, res)
            res.append(node.val)
            self.helper(node.right, res)


# Solution 2: Iterative
# Time: O(n), Space: O(n)

class Solution:
    def inorderTraversal(self, root: Optional[TreeNode]) -> List[int]:
        res = []
        stack = []
        curr = root
        while stack or curr:
            while curr:
                stack.append(curr)
                curr = curr.left
            curr = stack.pop()
            res.append(curr.val)
            curr = curr.right
        return res


# All DFS traversals:
# https://leetcode.com/explore/learn/card/data-structure-tree/134/traverse-a-tree/929/discuss/283746/All-DFS-traversals-(preorder-inorder-postorder)-in-Python-in-1-line

class Solution:
    def inorderTraversal(self, root: Optional[TreeNode]) -> List[int]:
        return self.inorderTraversal(root.left) + [root.val] + self.inorderTraversal(root.right) if root else []


# TODO:
# Add optimal Morris Traversal
