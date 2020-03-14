# -*- coding:utf-8 -*-
class Solution:
    def minNumberInRotateArray(self, rotateArray):
        # write code here
        if len(rotateArray) == 0:
            return 0
        left = 0
        right = len(rotateArray)-1
        while(left < right):
            if rotateArray[left] < rotateArray[right]:
                return rotateArray[left]
            mid = left + (right - left) // 2
            if rotateArray[mid] > rotateArray[left]:
                left = mid + 1
            elif rotateArray[mid] < rotateArray[right]:
                right = mid
            else:
                left += 1  
        return rotateArray[left]