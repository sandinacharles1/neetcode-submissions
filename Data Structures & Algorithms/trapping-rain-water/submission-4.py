class Solution:
    def trap(self, height: List[int]) -> int:
        left_tallest, right_tallest = 0,0
        left_tallest_index, right_tallest_index = 0,0
        left_index, right_index = 0, len(height) - 1
        rainwater = 0
        
        #We capture water with an optimistic approach that there is a taller wall to be found later on.
        #So, for each new BORDER (a border is defined as a new wall thats bigger than the previous tallest), we expect another BORDER, so we keep calculating as if we are the minimum
        #However, the same is happening on both sides. So, this discrepancy means one side might expect a larger border when in reality it only gets smaller from there. So, what we will do at the end is that we get the two most recently defined borders, then we get rid of any excess we may have optimistically calculated by subtracting the difference by the distance
        #We could be less optimisitc by moving the shorter pointers only when we know theres more on the pther side?
        while left_index < right_index:
            left_height, right_height = height[left_index], height[right_index]
            #this time, we dont move equally, we move the shortest to the tallest (the tallest is a grounded pivot point, in a way), so we can avoid optimisim and always know that we ARE at the minimum and we're moving towards a max
            if left_height < right_height:
                left_tallest = max(left_tallest, left_height)
                rainwater += (left_tallest - left_height)
                left_index += 1
            
            else:
                right_tallest = max(right_tallest, right_height)
                rainwater += (right_tallest - right_height)
                right_index -= 1
        
        return rainwater