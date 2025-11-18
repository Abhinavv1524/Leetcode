class Solution:
    def maximalRectangle(self, matrix: List[List[str]]) -> int:
        if not matrix or not matrix[0]:
            return 0
        
        cols = len(matrix[0])
        heights = [0] * cols
        max_area = 0
        
        def largestRectangleArea(heights):
            stack = []
            area = 0
            for i, h in enumerate(heights + [0]):
                while stack and heights[stack[-1]] > h:
                    height = heights[stack.pop()]
                    left = stack[-1] + 1 if stack else 0
                    width = i - left
                    area = max(area, height * width)
                stack.append(i)
            return area
        
        for row in matrix:
            for j in range(cols):
                heights[j] = heights[j] + 1 if row[j] == '1' else 0
            max_area = max(max_area, largestRectangleArea(heights))
        
        return max_area

