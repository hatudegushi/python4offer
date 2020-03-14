# -*- coding:utf-8 -*-
class Solution:
    # matrix类型为二维列表，需要返回列表
    def printMatrix(self, matrix):
        # write code here
        outlist = []
        while True:
            outlist.extend(matrix[0])
            if len(matrix) > 1:
                matrix = matrix[1:]
            else:
                break
            matrix = [[row[i] for row in matrix] for i in range(len(matrix[0])-1, -1, -1)]
        return outlist