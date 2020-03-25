# -*- coding:utf-8 -*-
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None
class Solution:
    def deep(self, pRoot):
        if pRoot == None:
            return 0
        left = self.deep(pRoot.left)
        if left == -1:
            return -1
        right = self.deep(pRoot.right)
        if right == -1:
            return -1
        if abs(left - right) > 1:
            return -1
        else:
            return max(left, right) + 1

    def IsBalanced_Solution(self, pRoot):
        # write code here
        return self.deep(pRoot) != -1        