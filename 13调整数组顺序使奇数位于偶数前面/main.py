# -*- coding:utf-8 -*-
class Solution:
    def reOrderArray(self, array):
        # write code here
        flag = True
        l = len(array)
        for i in range(l):
            for j in range(l-i-1):
                if array[j] & 1:
                    continue
                elif array[j+1] & 1:
                    array[j], array[j+1] = array[j+1], array[j]
                    flag = False
            if flag:
                break
        return array
