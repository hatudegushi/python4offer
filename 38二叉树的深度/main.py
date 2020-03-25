# -*- coding:utf-8 -*-
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None
class Solution:
    def __init__(self):
        self.count = 0
        self.max = 0
    
    def DFS(self, pRoot):
        if not pRoot:
            if self.count > self.max:
                self.max = self.count
            return
        self.count += 1
        self.DFS(pRoot.left)
        self.DFS(pRoot.right)
        self.count -= 1

    def TreeDepth(self, pRoot):
        # write code here
        self.DFS(pRoot)
        return self.max