class Solution:
    def maxArea(self, heights: List[int]) -> int:
        #initial thoughts:

        #start with first and last bars, calculate height, and
         #make this the intermediate return value
        #move the shorter bar to the next one and calculate
        #if it is more water replace the return value
        #repeat until the two bars are the same or they go past each other

        area = 0
        left = 0
        right = len(heights) - 1
        
        while(left < right):
            if(heights[left] <= heights[right]):
                area = max(area, ((right - left) * heights[left]))
                left += 1
            else:
                area = max(area, ((right - left) * heights[right]))
                right -= 1
        return area