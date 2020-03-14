# -*- coding:utf-8 -*-
class Solution:
    def Power(self, base, exponent):
        # write code here
        if exponent == 0:
            return 1
        flag = 0
        if exponent < 0:
            flag = 1
            exponent *= -1
        res = 1
        temp = base
        while exponent:
            if exponent & 1:
                res = res * temp
            temp = temp * temp
            exponent = exponent >> 1
        if flag:
            return 1 / res
        else:
            return res