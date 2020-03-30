# -*- coding:utf-8 -*-
# class ListNode:
#     def __init__(self, x):
#         self.val = x
#         self.next = None
class Solution:
    def EntryNodeOfLoop(self, pHead):
        # write code here
        fast, slow = pHead, pHead
        while fast.next != None and fast.next.next != None:
            fast = fast.next.next
            slow = slow.next
            if slow == fast:
                p = pHead
                while p != slow:
                    p = p.next
                    slow = slow.next
                return p
        return None