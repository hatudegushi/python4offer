# -*- coding:utf-8 -*-
import dis
class Solution:
    # 这里要特别注意~找到任意重复的一个值并赋值到duplication[0]
    # 函数返回True/False
    def duplicate(self, numbers, duplication):
        # write code here
        for i in range(len(numbers)):
            if i != numbers[i]:
                if numbers[i] != numbers[numbers[i]]:
                    numbers[numbers[i]], numbers[i] = numbers[i], numbers[numbers[i]]
                else:
                    duplication[0] = numbers[i]
                    return True
        return False

#关于a, b = b, a
#python中先存储b和a的值
#然后先将b的值赋给a，再将a的值赋给b
def fun1(l):
    l[0], l[l[0]] = l[l[0]], l[0]
    
def fun2(l):
    l[l[0]], l[0] = l[0], l[l[0]]

l = [2, 1, 0]
print(l)
fun1(l)
print(l)
fun2(l)
print(l)
# dis.dis(fun1)
# dis.dis(fun2)