# -*- coding:utf-8 -*-
class Solution:
    def IsPopOrder(self, pushV, popV):
        # write code here
        l = []
        for i in pushV:
            l.append(i)
            while l and l[-1] == popV[0]:
                l.pop()
                popV.pop(0)
        if popV:
            return False
        else:
            return True

s = Solution()
print(s.IsPopOrder([1,2,3,4,5],[4,5,3,2,1]))