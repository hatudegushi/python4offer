# -*- coding:utf-8 -*-
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None
class Solution:
    def IsSubtree(self, pRoot1, pRoot2):
        if not pRoot2:
            return True
        elif not pRoot1:
            return False
        elif pRoot1.val != pRoot2.val:
            return False
        else:
            return self.IsSubtree(pRoot1.left, pRoot2.left) and self.IsSubtree(pRoot1.right, pRoot2.right)

    def HasSubtree(self, pRoot1, pRoot2):
        # write code here
        if not pRoot1 or not pRoot2:
            return False
        res = self.IsSubtree(pRoot1, pRoot2)       
        if res:
            return True
        else:
            return self.HasSubtree(pRoot1.left, pRoot2) or self.HasSubtree(pRoot1.right, pRoot2)