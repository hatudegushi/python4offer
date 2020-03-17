# -*- coding:utf-8 -*-
class RandomListNode:
    def __init__(self, x):
        self.label = x
        self.next = None
        self.random = None
class Solution:
    # 返回 RandomListNode
    def Clone(self, pHead):
        # write code here
        if not pHead:
            return None
        newHead = RandomListNode(pHead.label)
        map_p = {pHead: newHead}

        p = pHead.next
        q = newHead
        while p:
            q.next = RandomListNode(p.label)
            map_p[p] = q.next
            p = p.next
            q = q.next

        p = pHead
        q = newHead
        while p:
            if p.random:
                q.random = map_p[p.random]
            p = p.next
            q = q.next
        return newHead

p = RandomListNode(1)
p.next = RandomListNode(2)
p.next.next = RandomListNode(3)
p.next.next.next = RandomListNode(4)
p.next.next.next.next = RandomListNode(5)
p.random = p.next.next
p.next.random = p.next.next.next.next
p.next.next.next.random = p.next

def printP(head):
    l = []
    p = head
    while p:
        l.append(p.label)
        p = p.next
    p = head
    while p:
        if p.random:
            l.append(p.random.label)
        else:
            l.append('#')
        p = p.next
    return l

new = Solution().Clone(p)
print(printP(p))
print(printP(new))