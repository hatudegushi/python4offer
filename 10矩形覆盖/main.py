# -*- coding:utf-8 -*-
class Solution:
    def rectCover(self, number):
        # write code here
        if number == 0:
            return 0
        if number == 1:
            return 1
        if number == 2:
            return 2
        l = [1, 2]
        i = 2
        while i < number:
            l.append(l[i-2] + l[i-1])
            i += 1
        return l[number-1]