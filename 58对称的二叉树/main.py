# -*- coding:utf-8 -*-
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None
class Solution:
    def isEqual(self, left, right):
        if left == None and right == None:
            return True
        if left == None or right == None:
            return False
        if left.val == right.val:
            return self.isEqual(left.left, right.right) and self.isEqual(left.right, right.left)
        else:
            return False
    def isSymmetrical(self, pRoot):
        # write code here
        if pRoot == None:
            return True
        return self.isEqual(pRoot.left, pRoot.right)