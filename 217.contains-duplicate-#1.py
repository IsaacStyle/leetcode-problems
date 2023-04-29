def containsDuplicate(self, nums):
        map = {}
        for num in nums:
            if num in map:
                return True
            map[num] = num
        return False