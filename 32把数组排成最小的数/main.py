# -*- coding:utf-8 -*-
import functools
def compare(s1, s2):
        m = s1 + s2
        n = s2 + s1
        if m > n:
            return 1
        elif m == n:
            return 0
        else:
            return -1

class Solution:
    def PrintMinNumber(self, numbers):
        # write code here
        if not numbers:
            return ''
        strlist = []
        for i in numbers:
            strlist.append(str(i))
        strlist.sort(key = functools.cmp_to_key(compare))
        s = ''
        for i in strlist:
            s += i
        return int(s)