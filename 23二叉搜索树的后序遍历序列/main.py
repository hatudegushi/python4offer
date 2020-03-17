# -*- coding:utf-8 -*-
class Solution:
    def assistance(self, sequence):
        if not sequence:
            return True
        position = 0
        while sequence[position] < sequence[-1]:
            position += 1
        i = position + 1
        length = len(sequence)
        while i < length:
            if sequence[i] < sequence[-1]:
                return False
            i += 1
        left = self.assistance(sequence[0:position])
        right = self.assistance(sequence[position:-1])
        return left and right

    def VerifySquenceOfBST(self, sequence):
        # write code here
        if not sequence:
            return False
        return self.assistance(sequence)