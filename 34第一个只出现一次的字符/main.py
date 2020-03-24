# -*- coding:utf-8 -*-
class Solution:
    def FirstNotRepeatingChar(self, s):
        # write code here
        two = []
        one = []
        for c in s:
            if c in one:
                one.pop(one.index(c))
                two.append(c)
            elif not c in two:
                one.append(c)
        if one:
            return s.index(one[0])
        else:
            return -1