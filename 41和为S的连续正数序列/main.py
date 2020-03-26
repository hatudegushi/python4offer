# -*- coding:utf-8 -*-
class Solution:
    def FindContinuousSequence(self, tsum):
        # write code here
        if tsum < 3:
            return []
        seq_list = []
        seq = []
        nsum = 0
        for i in range(1, tsum // 2 + 2):
            seq.append(i)
            nsum += i
            while nsum > tsum:
                nsum -= seq.pop(0)
            if nsum == tsum:
                seq_list.append(seq[:])
        return seq_list

print(Solution().FindContinuousSequence(9))