# -*- coding:utf-8 -*-
class Solution:
    # array 二维列表
    def Find(self, target, array):
    # write code hereF
        length = len(array)
        if length == 0 or len(array[0]) == 0:
            return False
        i = 0
        j = len(array[0]) - 1
        while i < length and j >= 0:
            if target < array[i][j]:
                j -= 1
            elif target > array[i][j]:
                i += 1
            else:
                return True
        return False

s = Solution()
print(s.Find(7,[[1,2,8,9],[2,4,9,12],[4,7,10,13],[6,8,11,15]]))