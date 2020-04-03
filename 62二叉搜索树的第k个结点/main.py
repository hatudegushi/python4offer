# -*- coding:utf-8 -*-
class TreeNode:
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None
class Solution:
    def __init__(self):
        self.node = None
        self.i = 0
    def helper(self, pRoot, k):
        if not pRoot:
            return
        self.helper(pRoot.left, k)
        self.i += 1
        if self.i == k:
            self.node = pRoot
            return
        self.helper(pRoot.right, k)
    # 返回对应节点TreeNode
    def KthNode(self, pRoot, k):
        # write code here
        self.i = 0
        self.helper(pRoot, k)
        return self.node

root = TreeNode(8)
root.left = TreeNode(6)
root.right = TreeNode(10)
root.left.left = TreeNode(5)
root.left.right = TreeNode(7)
root.right.left = TreeNode(9)
root.right.right = TreeNode(11)

print(Solution().KthNode(root, 1))