def threeSum(self, nums):
        output = []
        nums.sort()
        for i,num in enumerate(nums):
            if num > 0: break
            if i > 0 and num == nums[i - 1]: continue
            l, r = i + 1, len(nums) - 1
            while l < r:
                curr = num + nums[l] + nums[r]
                if curr < 0: l += 1
                elif curr > 0: r -= 1
                else: 
                    output.append([num, nums[l], nums[r]]) 
                    l += 1
                    r -= 1
                    while nums[l] == nums[l - 1] and l < r:
                        l += 1
        return output