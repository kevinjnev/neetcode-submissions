class Solution:
    def trap(self, height: List[int]) -> int:
        if len(height) == 0:
            return 0

        left = 0
        right = len(height) - 1

        area = 0
        max_left = height[left]
        max_right = height[right]
        
        while left < right:
            if max_left <= max_right:
                left += 1
                max_left = max(max_left, height[left])
                area += max_left - height[left]
            else:
                right -= 1
                max_right = max(max_right, height[right])
                area += max_right - height[right]

        return area