# -*- coding:utf-8 -*-
class Solution:
    # 返回[a,b] 其中ab是出现一次的两个数字
    def FindNumsAppearOnce(self, array):
        # write code here
        nums_dict = {}
        for i in range(len(array)):
            try:
                del nums_dict[array[i]]
            except KeyError:
                nums_dict[array[i]] = 1
        return nums_dict.keys()