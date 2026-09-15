class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        #Explanation: We slide the window for two criterias LOCALLY. When we find our local minimum (aka our minimum at that point in time), we put out left pointer towards it because max means lowest value, we auto increment the right. IF WE DONT reach another local minimum, we just keep going in gettings hopes of an even greater max profit. By this point, we saved our local max profit, if we get a new minimum that has a bummy maximum after it, we already have our maximimum from earlier saved. If we get a new minimum WITH a new maximum thats good, excellent!
        
        #Method:
        #Gain a local min, always put left pointer there. Always update the left pointer to min. That's the only incrememntation you do
        #Auto increment the right, so you can alwyas see if theres new minimums or maximums and save thems. SO the right is allways incremented. The right goes up to the max in the list, the left is just there.


        #Implementation: 
        
        #Initialize the minimimum as the first
        maxP, minBuy = 0, prices[0]

        #We will utilize the right pointer by just looping through as usual. autoincrmemeenting the right, then we can just calculate maximums as per usual, and also by getting the minimum
        for i, val in enumerate(prices): 
            minBuy = min(minBuy, val) #Whenever the value is less than the minimum, oncrement the minBuy
            maxP = max(maxP, val - minBuy) #always calculate max
           
        return maxP
