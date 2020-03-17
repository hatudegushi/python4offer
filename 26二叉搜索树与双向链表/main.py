# -*- coding:utf-8 -*-
class TreeNode:
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None
class Solution:
    def __init__(self):
        self.pointer = None

    def inorder(self, curNode):
        if not curNode:
            return
        self.inorder(curNode.left)
        curNode.left = self.pointer
        if self.pointer:
            self.pointer.right = curNode
        self.pointer = curNode
        self.inorder(curNode.right)

    def Convert(self, pRootOfTree):
        # write code here
        if not pRootOfTree:
            return None
        self.inorder(pRootOfTree)
        root = self.pointer
        while root.left:
            root = root.left
        return root