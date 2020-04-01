# -*- coding:utf-8 -*-
# class TreeLinkNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None
#         self.next = None
class Solution:
    def GetNext(self, pNode):
        # write code here
        if pNode.right:
            p = pNode.right
            while p.left:
                p = p.left
            return p
        else:
            if pNode.next != None and pNode.next.left == pNode:
                return pNode.next
            else:
                p = pNode.next
                while p and p.next:
                    if p.next.left == p:
                        return p.next
                    p = p.next
                return None