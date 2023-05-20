def longestConsecutive(self, nums):
        sort = sorted(nums)
        max_len = 1
        curr = 1
        if not len(nums): return 0
        for i in range(1,len(nums)):
            j = sort[i]
            if j - 1 == sort[i - 1]:
                curr += 1
                max_len = max(max_len,curr)
            elif j == sort[i - 1]:
                continue
            else:
                curr = 1
        return max_len