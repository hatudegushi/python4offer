# -*- coding:utf-8 -*-
class TreeNode:
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None
class Solution:
    def Serialize(self, root):
        # write code here
        if not root:
            return '#!'
        queue = [root]
        empty = TreeNode('#')
        res = ''
        flag = True
        while flag:
            flag = False
            for _ in range(len(queue)):
                tmp = queue.pop(0)
                res += str(tmp.val) + '!'
                if tmp.left:
                    flag = True
                    queue.append(tmp.left)
                else:
                    queue.append(empty)
                if tmp.right:
                    flag = True
                    queue.append(tmp.right)
                else:
                    queue.append(empty)
        return res

    def Deserialize(self, s):
        # write code here
        i = 0
        j = 0
        while s[j] != '!':
            j += 1
        if s[i:j] == '#':
            return None
        root = TreeNode(int(s[i:j]))
        empty = TreeNode('#')
        queue = [root]
        length = len(s) - 1
        while j < length:
            tmp = queue.pop(0)
            i = j + 1
            j = j + 1
            while s[j] != '!':
                j += 1
            if s[i:j] != '#':
                tmp.left = TreeNode(int(s[i:j]))
                queue.append(tmp.left)
            else:
                queue.append(empty)
            
            i = j + 1
            j = j + 1
            while s[j] != '!':
                j += 1
            if s[i:j] != '#':
                tmp.right = TreeNode(int(s[i:j]))
                queue.append(tmp.right)
            else:
                queue.append(empty)
        return root

root = TreeNode(1)
root.left = TreeNode(2)
root.right = TreeNode(3)
# root.left.left = TreeNode(4)
root.left.right = TreeNode(5)

s = Solution().Serialize(root)

newroot = Solution().Deserialize(s)
queue = [newroot]
while queue:
    for _ in range(len(queue)):
        node = queue.pop(0)
        print(node.val)
        if node.left:
            queue.append(node.left)
        if node.right:
            queue.append(node.right)