# -*- coding:utf-8 -*-
class Solution:
    def cutRope(self, number):
        # write code here
        if number == 2:
            return 1
        if number == 3:
            return 2
        c = number % 3
        if c == 0:
            return 3 ** (number // 3)
        elif c == 1:
            return 3 ** ((number // 3) - 1) * 2 * 2
        elif c == 2:
            return 3 ** (number // 3) * 2