# -*- coding:utf-8 -*-
class Solution:
    def __init__(self):
        self.count = 0
    def movingCount(self, threshold, rows, cols):
        # write code here
        m = [[0 for j in range(cols)] for i in range(rows)]
        def judge(i, j):
            s = sum(map(int,str(i)+str(j)))
            return s <= threshold
        self.count = 0
        def traverse(i, j):
            if not (0<=i<rows and 0<=j<cols):
                return
            if m[i][j] == 0 and judge(i, j):
                self.count += 1
                m[i][j] = 1
                traverse(i-1, j)
                traverse(i+1, j)
                traverse(i, j-1)
                traverse(i, j+1)
        traverse(0, 0)
        return self.count