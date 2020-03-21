# -*- coding:utf-8 -*-
class Solution:
    def FindGreatestSumOfSubArray(self, array):
        # write code here
        if not array:
            return 0
        maxlist = []
        maxnum = array[0]
        for i in range(len(array)):
            if i == 0 or maxlist[i-1] < 0 :
                maxlist.append(array[i])
            elif maxlist[i-1] > 0:
                maxlist.append(array[i] + maxlist[i-1])
            if maxnum < maxlist[i]:
                maxnum = maxlist[i]
        return maxnum

print(Solution().FindGreatestSumOfSubArray([1,-2,3,10,-4,7,2,-5]))