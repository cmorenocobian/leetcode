'''
https://leetcode.com/problems/symmetric-tree
'''


# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def isSymmetric(self, root: Optional[TreeNode]) -> bool:
        if not root:
            return True
        return self.simetric_branch(root.left, root.right)
    
    def simetric_branch(self, left_branch, right_branch):
        if left_branch is None and right_branch is None:
            return True
        elif left_branch is None or right_branch is None:
            return False
        if left_branch.val != right_branch.val:
            return False
        return self.simetric_branch(left_branch.left, right_branch.right) and self.simetric_branch(left_branch.right, right_branch.left)