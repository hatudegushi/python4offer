# -*- coding:utf-8 -*-
class ListNode:
    def __init__(self, x):
        self.val = x
        self.next = None
class Solution:
    # 返回合并后列表
    def Merge(self, pHead1, pHead2):
        # write code here
        newlist = ListNode(-1)
        cur = newlist
        while pHead1 and pHead2:
            if pHead1.val > pHead2.val:
                cur.next = ListNode(pHead2.val)
                pHead2 = pHead2.next
            else:
                cur.next = ListNode(pHead1.val)
                pHead1 = pHead1.next
            cur = cur.next       
        if pHead1:
            cur.next = pHead1
        elif pHead2:
            cur.next = pHead2
        return newlist.next