# -*- coding:utf-8 -*-
class Solution:
    def maxInWindows(self, num, size):
        # write code here
        if size == 0:
            return []
        i = 0
        j = size - 1
        res = []
        length = len(num)
        while j < length:
            temp = num[i]
            for n in range(i, j+1):
                if temp < num[n]:
                    temp = num[n]
            res.append(temp)
            i += 1
            j += 1
        return res