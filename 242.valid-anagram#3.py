def isAnagram(self, s, t):
        if len(s) != len(t): return False
        mapS = {}
        mapT = {}

        for i in range(len(s)):
            mapS[s[i]] = mapS.get(s[i],0) + 1
            mapT[t[i]] = mapT.get(t[i],0) + 1
        
        return mapS == mapT