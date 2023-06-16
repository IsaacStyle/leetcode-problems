def maxArea(self, height):
        largest = 0
        l, r = 0, len(height) - 1
        while l < r:
            largest = max(largest, min(height[l],height[r]) * (r - l))
            if height[l] > height[r]: r -= 1
            else: l += 1
        return largest