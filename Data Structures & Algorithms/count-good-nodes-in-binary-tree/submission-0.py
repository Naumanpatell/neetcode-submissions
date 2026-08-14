# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def goodNodes(self, root: TreeNode) -> int:
        good_node = 0
        
        def dfs(node, curr_max):
            nonlocal good_node

            if node is None:
                return None 

            if node.val >= curr_max:
                good_node += 1
                curr_max = node.val
            
            dfs(node.left, curr_max)
            dfs(node.right, curr_max)

        dfs(root, root.val)
        return good_node
