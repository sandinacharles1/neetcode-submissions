class Solution:
    def findKthLargest(self, nums: List[int], k: int) -> int:
        return heapq.nlargest(k, nums)[-1] #Get the largest k, and get the smallest (descending order) to get the k-th insteaf of the max