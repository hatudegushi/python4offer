# -*- coding:utf-8 -*-
class Solution:
    def GetLeastNumbers_Solution(self, tinput, k):
        # write code here
        length = len(tinput)
        if length < k:
            return []
        for i in range(k):
            for j in range(length-i-1, 0, -1):
                if tinput[j] < tinput[j-1]:
                    tinput[j], tinput[j-1] = tinput[j-1], tinput[j]
        return tinput[:k]