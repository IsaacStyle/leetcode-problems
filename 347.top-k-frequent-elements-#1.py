def topKFrequent(self, nums, k):
        output = []
        map = {}
        for i in nums:
            map[i] = map.get(i,0) + 1
        sorted_map = sorted(map.items(), key=lambda x: x[1], reverse = True)
        for i in range(k):
            output.append(sorted_map[i][0])
        return output