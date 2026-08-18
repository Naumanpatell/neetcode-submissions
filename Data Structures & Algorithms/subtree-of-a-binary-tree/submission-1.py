# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:   
    def isSubtree(self, root: Optional[TreeNode], subroot: Optional[TreeNode]) -> bool:

        def SameTree(p,q):
            if not p and not q:
                return True
            if not p or not q or p.val != q.val:
                return False
            return SameTree(p.left,q.left) and SameTree(p.right,q.right)

        def isSubtreeHelper(root,subroot):
            if not root:
                return False
            if SameTree(root,subroot):
                return True
            return isSubtreeHelper(root.left,subroot) or isSubtreeHelper(root.right,subroot)
        
        return isSubtreeHelper(root,subroot)

# Forgot the base case in the helper function and messed up the return statement in the helper function as well samesize func perfect
        
        