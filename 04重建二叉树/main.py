# -*- coding:utf-8 -*-
class TreeNode:
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None
    def print(self):
        pass

class Solution:
    # 返回构造的TreeNode根节点
    def reConstructBinaryTree(self, pre, tin):
        # write code here
        if len(pre) == 0:
            return
        if len(pre) == 1:
            return TreeNode(pre[0])
        root = TreeNode(pre[0])
        key = tin.index(pre[0])
        root.left = self.reConstructBinaryTree(pre[1:key + 1], tin[:key])
        root.right = self.reConstructBinaryTree(pre[key + 1:], tin[key + 1:])
        return root

s = Solution()
node = s.reConstructBinaryTree([1,2,3,4,5,6,7],[3,2,4,1,6,5,7])