# -*- coding:utf-8 -*-
class Solution:
    def LastRemaining_Solution(self, n, m):
        # write code here
        if n == 0:
            return -1
        s = 0
        for i in range(2, n+1):
            s = (s+m)%i
        return s