# -*- coding:utf-8 -*-
class Solution:
    def __init__(self):
        self.s1 = []
        self.s2 = []

    def push(self, node):
        # write code here
        self.s1.append(node)

    def pop(self):
        # return xx
        if not self.s2:
            while self.s1:
                self.s2.append(self.s1.pop(-1))
        return self.s2.pop(-1)