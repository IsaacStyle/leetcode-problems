def groupAnagrams(self, strs):
        map = collections.defaultdict(list)

        for i in strs:
            map[tuple(sorted(i))].append(i)

        return map.values()