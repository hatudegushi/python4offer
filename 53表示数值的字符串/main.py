# -*- coding:utf-8 -*-
import re

class Solution:
    # s字符串
    def isNumeric(self, s):
        # write code here
        match = re.match(r'^[-+]?\d*(?:\.\d*)?(?:[eE][+\-]?\d+)?$', s)
        if match:
            return True
        else:
            return False

print(Solution().isNumeric('12.4e3'))