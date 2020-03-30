# -*- coding:utf-8 -*-
from ctypes import *
class Solution:
    def Add(self, num1, num2):
        # write code here
        while num2:
            temp = c_int(num1 ^ num2).value
            num2 = c_int((num1 & num2) << 1).value
            num1 = temp
        return num1