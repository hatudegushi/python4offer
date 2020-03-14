# -*- coding:utf-8 -*-
class Solution:
    def jumpFloorII(self, number):
        # write code here
        n = 1
        number -= 1
        while number:
            n = n * 2
            number -= 1
        return n