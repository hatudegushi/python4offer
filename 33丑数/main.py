# -*- coding:utf-8 -*-
class Solution:
    def GetUglyNumber_Solution(self, index):
        # write code here
        if index == 0:
            return 0
        l = [1]
        for i in range(index):
            if not 2*l[i] in l:
                l.append(2*l[i])
            if not 3*l[i] in l:
                l.append(3*l[i])
            if not 5*l[i] in l:
                l.append(5*l[i])
            l.sort()
        return l[index-1]

print(Solution().GetUglyNumber_Solution(1))