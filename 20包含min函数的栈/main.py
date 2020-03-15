# -*- coding:utf-8 -*-
class Solution:
    def __init__(self):
        self.stack = []
        self.mstack = []
    def push(self, node):
        # write code here
        self.stack.append(node)
        if not self.mstack:
            self.mstack.append(node)
        else:
            if self.mstack[-1] < node:
                self.mstack.append(self.mstack[-1])
            else:
                self.mstack.append(node)
    def pop(self):
        # write code here
        if self.stack:
            self.stack.pop()
            self.mstack.pop()

    def top(self):
        # write code here
        if self.stack:
            return self.stack[-1]
        else:
            return []

    def min(self):
        # write code here
        if self.mstack:
            return self.mstack[-1]
        else:
            return []