# -*- coding:utf-8 -*-
class Solution:
    def Fibonacci(self, n):
        # write code here
        if n == 0:
            return 0
        if n == 1:
            return 1
        l = [0, 1]
        i = 1
        while i < n:
            l.append(l[i-1] + l[i])
            i += 1
        return l[n]