def isValid(self, s):
        map = {
            '(':0,
            '[':0,
            '{':0
        }
        for i,char in enumerate(s):
            
            if char in map:
                map[char] += 1
                print(map[char])
            if char == ')':
                map['('] -= 1
                if map['('] < 0: return False
            if char == ']':
                map['['] -= 1
                if map['['] < 0: return False
            if char == '}':
                map['{'] -= 1
                if map['{'] < 0: return False
        return True