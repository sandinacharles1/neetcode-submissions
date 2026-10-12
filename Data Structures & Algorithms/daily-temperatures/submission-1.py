class Solution:
    def dailyTemperatures(self, temperatures: List[int]) -> List[int]:
        days_until_warmer = [0] * len(temperatures)
        stack = [] #LIFO because when we get a valuee closer to the most recent, we address that first since that's added last
        #logic. We appen a value and their index to the stack. WE look at this same stack whenever we want to check if a value is grater than another. If we keep popping from the stack, we can eassily detect the values that found their highest quickly, but by having the older ones who may need a bigger value, we 
        for current_index, current_temperature in enumerate(temperatures):
            
            while stack and current_temperature > stack[-1][1]:
                previous_index, previous_temperature = stack.pop()
                distance = current_index - previous_index
                days_until_warmer[previous_index] = distance
            
            stack.append((current_index, current_temperature))
        return days_until_warmer

'''
Explanation:
stack =[] WE use a last-in-first out. Why? Because, we want to start by updating the most recent item to us, see if it's less than. Otherwise, we know the other numbers before are most likely also greater than because we are less than the most recent number. If that number was greater thsn the previous, the code would've run. However, if we are greater than the previous, we pop it,get our distance from them, and keep going by going backwward to see if we are greater than the previous numbers. Then we get the distance

It's a simple concept, with your number, compare to past numbers using stack (no need for hashmap because we want to get rid of numbers we find the next hottest day of. if we find the next hottest day for them then they're out the need.). We don't need a queue because it is guarenteed the items in our stack is in non-increasing order. so, if we are bigger than the previous, we can assure we are bigger than the ones before
'''