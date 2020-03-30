# -*- coding:utf-8 -*-
class Solution:
    # 返回对应char
    def __init__(self):
        self.s = ''
        self.map = {}

    def FirstAppearingOnce(self):
        # write code here
        for c in self.s:
            if self.map[c] == 1:
                return c
        return '#'

    def Insert(self, char):
        # write code here
        self.s += char
        if char in self.map:
            self.map[char] += 1
        else:
            self.map[char] = 1