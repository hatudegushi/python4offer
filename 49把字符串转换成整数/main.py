# -*- coding:utf-8 -*-
class Solution:
    def StrToInt(self, s):
        # write code here
        str_dict = {
            '0': 0,
            '1': 1,
            '2': 2,
            '3': 3,
            '4': 4,
            '5': 5,
            '6': 6,
            '7': 7,
            '8': 8,
            '9': 9,
            '+': -1,
            '-': -1,
            }
        n = 0
        flag = 1
        for c in s:
            if c in str_dict:
                if c == '+':
                    continue
                elif c == '-':
                    flag = -1
                else:
                    n = n * 10 + str_dict[c]
            else:
                return 0
        if -0x80000000 <= n*flag <= 0x7FFFFFFF:
            return n*flag
        else:
             return 0