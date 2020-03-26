# -*- coding:utf-8 -*-
class Solution:
    def FindNumbersWithSum(self, array, tsum):
        # write code here
        low = 0
        high = len(array) - 1
        while low < high:
            nsum = array[low] + array[high]
            if nsum > tsum:
                high -= 1
            elif nsum < tsum:
                low += 1
            else:
                return [array[low], array[high]]
        return []