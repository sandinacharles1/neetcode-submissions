class Solution:
    def maxArea(self, heights: List[int]) -> int:
        #1. start from max width (usually max unless bars arent) until you get big width and height. 
        l, r = 0, len(heights) - 1
        max_area = 0
        
        #2. Start two pointers from opposite side
        while l < r:
            width = r - l
            height = min(heights[r],heights[l]) #prevent overflow
            area = width * height

            #3. Replace max area if its the current maximum
            max_area = max(max_area, area)

            #4. Get rid of the bar with the shortest height. So if the short bar is left, move up on left. 
            if heights[l] <= heights[r]:
                l +=1 
            else: 
                r -= 1
        return max_area