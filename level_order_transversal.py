'''
https://leetcode.com/problems/binary-tree-level-order-traversal/
'''

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
        # Create 2 lists, first to store the values of each level, and the second to store the nodes of the current level
        transversal_order=[]
        nodes_in_level=[root]

        while nodes_in_level:
            # Store the values of each node in this list
            values=[]
            # If there are nodes inside the current node store them
            next_level=[]

            # Go over each level, store the values and the leaves (inferior nodes)
            for node in nodes_in_level:
                values.append(node.val)
                if (node.left is not None):
                    next_level.append(node.left)
                if (node.right is not None):
                    next_level.append(node.right)
            transversal_order.append(values)
            nodes_in_level=next_level
        
        return transversal_order
    

