class Solution(object):
    def isValid(self, s):
        map = {
            '(':0,
            '[':0,
            '{':0
        }
        check = 0
        for i,char in enumerate(s):
            if len(s) % 2 != 0: return False
            if char in map:
                map[char] += 1
                check += 1
            if char == ')':
                check -= 1
                map['('] -= 1
                if map['('] < 0: return False
                if s[i-1] in map and s[i-1] != '(': return False
            if char == ']':
                check -= 1
                map['['] -= 1
                if map['['] < 0: return False
                if s[i-1] in map and s[i-1] != '[': return False
            if char == '}':
                check -= 1
                map['{'] -= 1
                if map['{'] < 0: return False
                if s[i-1] in map and s[i-1] != '{': return False
        if check == 0: return True