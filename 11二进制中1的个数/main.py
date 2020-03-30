# -*- coding:utf-8 -*-
from ctypes import *
class Solution:
    def NumberOf1(self, n):
        # write code here
        count = 0
        while c_int(n).value:
            count += 1
            n = n & (n-1)
            print(c_int(n).value, n)
        return count

print(Solution().NumberOf1(-4))