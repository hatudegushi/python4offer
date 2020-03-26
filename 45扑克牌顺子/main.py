# -*- coding:utf-8 -*-
class Solution:
    def IsContinuous(self, numbers):
        # write code here
        if not numbers:
            return False
        numbers.sort()
        zero = 0
        tag = 0
        for i in range(len(numbers)):
            if numbers[i] == 0:
                zero += 1
                tag = 0
            else:
                if tag:
                    if numbers[i-1] == numbers[i]:
                        return False
                    else:
                        zero -= numbers[i] - numbers[i-1] - 1
                        if zero < 0:
                            return False
                tag = 1           
        return True

print(Solution().IsContinuous([0,3,2,6,4]))