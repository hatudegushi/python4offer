# -*- coding:utf-8 -*-
class Solution:
    def isPath(self, matrix, rows, cols, path, i, j):
        if path == '':
            return True
        if matrix[i*cols+j] == path[0]:
            matrix[i*cols+j] = ''
            return len(path) == 1 or \
                    (i-1>=0 and self.isPath(matrix, rows, cols, path[1:], i-1, j)) or \
                    (i+1<rows and self.isPath(matrix, rows, cols, path[1:], i+1, j)) or \
                    (j-1>=0 and self.isPath(matrix, rows, cols, path[1:], i, j-1)) or \
                    (j+1<cols and self.isPath(matrix, rows, cols, path[1:], i, j+1))
        else:
            return False

    def hasPath(self, matrix, rows, cols, path):
        # write code here
        for i in range(rows):
            for j in range(cols):
                if self.isPath(list(matrix), rows, cols, path, i, j):
                    return True
        return False