# -*- coding:utf-8 -*-
class Solution:
    def Permutation(self, ss):
        # write code here
        length = len(ss)
        if length <= 1:
            return ss
        res = []
        for i in range(length):
            lists = self.Permutation(ss[:i]+ss[i+1:])
            for sublist in lists:
                l = ss[i] + sublist
                if l not in res:
                    res.append(l)
        return res