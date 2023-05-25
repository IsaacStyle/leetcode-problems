def longestConsecutive(self, nums):
        nums_set = set(nums)
        beegest = 0

        for n in nums_set:
            length = 0
            if n - 1 not in nums_set:
                while n + length in nums_set:
                    length += 1
                    beegest = max(beegest, length)
        return beegest