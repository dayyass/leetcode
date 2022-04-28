# Time: O(n), Space: O(n)

class Solution:
    def levelOrder(self, root: Optional[TreeNode]) -> List[List[int]]:
        res = []
        level = [root]
        while level:
            curr_vals = []
            next_level = []
            for node in level:
                if node:
                    curr_vals.append(node.val)
                    next_level.append(node.left)
                    next_level.append(node.right)
            if curr_vals:
                res.append(curr_vals)
            level = next_level
        return res
