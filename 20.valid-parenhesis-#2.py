class Solution(object):
    def isValid(self, s):
        if len(s) % 2 != 0: return False
        map = {'(':')', '{':'}','[':']'}
        stack = []
        for i in s:
            if i in map:  # 1
                stack.append(i)
            elif len(stack) == 0 or map[stack.pop()] != i:  # 2
                return False
        return len(stack) == 0 # 3