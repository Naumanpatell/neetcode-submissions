# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def levelOrder(self, root: Optional[TreeNode]) -> List[List[int]]:
        if root is None:
            return []
        
        result = []
        queue = [root]

        while queue:
            samelvl = []

            for i in range(len(queue)):
                node = queue.pop(0)
                samelvl.append(node.val)

                if node.left:
                    queue.append(node.left)
                if node.right:
                    queue.append(node.right)
            

            result.append(samelvl)
        return result 

#Revised today but forgot to actually do extraction of the node and literally used node to the code forward. LOGIC CORRECT



