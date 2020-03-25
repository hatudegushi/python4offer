# -*- coding:utf-8 -*-
class Solution:
    def binSearch(self, data, k):
        low = 0
        high = len(data) - 1 
        while low <= high:
            mid = high - (high-low) // 2
            if data[mid] < k:
                low = mid + 1
            elif data[mid] > k:
                high = mid - 1
            else:
                return mid
        return None

    def GetNumberOfK(self, data, k):
        # write code here
        local = self.binSearch(data, k)
        if local == None:
            return 0
        m, n = local, local
        while n > -1 and data[n] == k:
            n -= 1
        while m < len(data) and data[m] == k:
            m += 1
        return m - n - 1

print(Solution().GetNumberOfK([3], 3))