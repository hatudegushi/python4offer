# -*- coding:utf-8 -*-
class ListNode:
    def __init__(self, x):
        self.val = x
        self.next = None
class Solution:
    # 返回ListNode
    def ReverseList(self, pHead):
        # write code here
        if not pHead:
            return None
        pre = pHead
        post = pre.next
        pre.next = None
        while post:
            temp = post.next
            post.next = pre
            pre = post
            post = temp
        return pre

head = ListNode(1)
head.next = ListNode(2)
s = Solution()
newhead = s.ReverseList(head)
while newhead:
    print(newhead.val)
    newhead = newhead.next