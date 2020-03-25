# -*- coding:utf-8 -*-
class Solution:
    def __init__(self):
        self.count = 0

    def mergeSort(self, data):
        length = len(data)
        if length < 2:
            return data
        mid = length // 2
        left = self.mergeSort(data[:mid])
        right = self.mergeSort(data[mid:])
        i, j = 0, 0
        temp = []
        while i < len(left) and j < len(right):
            if left[i] < right[j]:
                temp.append(left[i])
                i += 1
            else:
                temp.append(right[j])
                j += 1
                self.count += len(left) - i
        return temp + left[i:] + right[j:]

    def InversePairs(self, data):
        # write code here
        self.mergeSort(data)
        return self.count % 1000000007