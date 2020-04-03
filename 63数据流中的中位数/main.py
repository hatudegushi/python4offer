# -*- coding:utf-8 -*-
class Solution:
    def __init__(self):
        self.numbers = []
        self.count = 0
    def Insert(self, num):
        # write code here
        self.numbers.append(num)
        self.count += 1

    def GetMedian(self, numbers):
        # write code here
        self.numbers.sort()
        if self.count % 2 == 1:
            return self.numbers[self.count // 2]
        else:
            return (self.numbers[self.count // 2] + self.numbers[self.count // 2 - 1]) / 2.0