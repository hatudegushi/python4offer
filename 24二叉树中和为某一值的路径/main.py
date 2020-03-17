# -*- coding:utf-8 -*-
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None
class Solution:
    # 返回二维列表，内部每个列表表示找到的路径
    def __init__(self):
        self.result_all = []
        self.array = []
    def FindPath(self, root, expectNumber):
        # write code here
        if not root:
            return []
        self.array.append(root.val)
        value = expectNumber - root.val
        if not value and not root.left and not root.right:
            self.result_all.append(self.array[:])
        self.FindPath(root.left, value)
        self.FindPath(root.right, value)
        self.array.pop()
        return self.result_all