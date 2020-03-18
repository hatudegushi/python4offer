# -*- coding:utf-8 -*-
class Solution:
    def MoreThanHalfNum_Solution(self, numbers):
        # write code here
        if not numbers:
            return 0
        count = 0
        num = None
        for i in numbers:
            if count == 0:
                num = i
                count = 1
            elif num == i:
                count += 1
            else:
                count -= 1
        count = 0
        for i in numbers:
            if num == i:
                count += 1
        if count > len(numbers) / 2:
            return num
        else:
            return 0

print(Solution().MoreThanHalfNum_Solution([1,2,3,2,2,2,5,4,2]))