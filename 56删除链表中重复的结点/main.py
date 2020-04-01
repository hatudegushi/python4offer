# -*- coding:utf-8 -*-
class ListNode:
    def __init__(self, x):
        self.val = x
        self.next = None
class Solution:
    def deleteDuplication(self, pHead):
        # write code here
        p = None
        q = pHead
        while q != None and q.next != None:
            if q.val == q.next.val:
                while q.next != None and q.val == q.next.val:
                    q = q.next
                if p:
                    p.next = q.next
                else:
                    pHead = q.next
                q = q.next
            else:
                p = q
                q = q.next
        return pHead

phead = ListNode(1)
p = phead
for i in (2,3,3,4,4):
    p.next = ListNode(i)
    p = p.next
p = Solution().deleteDuplication(phead)
while p:
    print(p.val)
    p = p.next