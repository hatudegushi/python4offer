# -*- coding:utf-8 -*-
# class ListNode:
#     def __init__(self, x):
#         self.val = x
#         self.next = None
class Solution:
    def FindFirstCommonNode(self, pHead1, pHead2):
        # write code here
        m = 0
        n = 0
        p = pHead1
        while p:
            m += 1
            p = p.next
        p = pHead2
        while p:
            n += 1
            p = p.next
        p = pHead1
        q = pHead2
        if m > n:
            for i in range(m-n):
                p = p.next
        else:
            for i in range(n-m):
                q = q.next
        while p:
            if p == q:
                return p
            p = p.next
            q = q.next
        return None