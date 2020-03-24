# -*- coding:utf-8 -*-
class Solution:
    def NumberOf1Between1AndN_Solution(self, n):
        # write code here
        res = 0
        i = 1
        while n // i != 0:
            h = n // (i*10)
            m = (n//i) % 10
            l = n % i
            if m == 0:
                res += h * i
            elif m == 1:
                res += h * i + l + 1
            elif m > 1:
                res += (h+1) * i
            i *= 10
        return res