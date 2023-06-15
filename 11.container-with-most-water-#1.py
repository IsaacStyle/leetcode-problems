def maxArea(self, height):
        largest = 0
        area = 0
        l, r = 0, len(height) - 1
        while l < r:
            low = min(height[l],height[r])
            area = low * (r - l)
            largest = max(largest,area)
            if height[l] > height[r]: r -= 1
            else: l += 1
        return largest