def twoSum(self, numbers, target):
        l, r = 0, len(numbers) - 1
        while l < r:
            curr = numbers[l] + numbers[r]
            if curr > target: r -= 1
            elif curr < target: l += 1
            elif curr == target: return [l + 1,r + 1]