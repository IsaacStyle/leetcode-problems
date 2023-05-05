def groupAnagrams(self, strs):
        map = {}
        for i in strs:
            sort = "".join(sorted(i))
            map[sort] = map.get(sort,[])
            map[sort].append(i)
        return map.values()