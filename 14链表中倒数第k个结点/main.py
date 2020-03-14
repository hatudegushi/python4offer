# -*- coding:utf-8 -*-
class ListNode:
    def __init__(self, x):
        self.val = x
        self.next = None

class Solution:
    def FindKthToTail(self, head, k):
        # write code here
        pre = head
        post = head
        for i in range(k):
            if not post:
                return None
            post = post.next
        while post != None:
            pre = pre.next
            post = post.next
        return pre