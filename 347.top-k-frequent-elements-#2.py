def topKFrequent(self, nums, k):
        map = {}
        freq = [[] for i in range(len(nums) + 1)]
        output = []
        for i in nums:
            map[i] = map.get(i,0) + 1
        for num,i in map.items():
            freq[i].append(num)
        
        for i in range(len(freq) - 1, 0, -1):
            for n in freq[i]:
                output.append(n)
            if len(output) == k:
                return output