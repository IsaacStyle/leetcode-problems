def isAnagram(self, s, t):
        map = {}
        if len(s) != len(t): return False
        for i in s:
            map[i] = map.get(i,0) + 1
        for j in t:
            if map.get(j,0) > 0:
                map[j] -= 1
            else: return False
        return True