class Solution:
    # s 源字符串
    def replaceSpace(self, s):
        # write code here
        new = s.replace(' ', '%20')
        return new