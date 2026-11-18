class Solution:
    def maxArea(self, heights: List[int]) -> int:
        max_area = max_left = max_right = -1
        left, right = 0, len(heights)-1

        while left<right:
            area = (right-left) * min(heights[left],heights[right])
            if area > max_area:
                max_left, max_right, max_area = left, right, area
            
            if heights[left]<heights[right]:
                left+=1                
            else:
                right-=1

        return max_area