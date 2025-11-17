from typing import List

class Solution:
    def largestRectangleArea(self, heights: List[int]) -> int:
        stack = []
        max_area = 0
        for i, h in enumerate(heights + [0]):
            while stack and (heights[stack[-1]] > h):
                height = heights[stack.pop()]
                left = stack[-1] + 1 if stack else 0
                width = i - left
                max_area = max(max_area, height * width)
            stack.append(i)
        return max_area
