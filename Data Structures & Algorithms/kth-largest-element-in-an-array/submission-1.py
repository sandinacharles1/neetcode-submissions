class Solution:
    def findKthLargest(self, nums: List[int], k: int) -> int:
        return heapq.nlargest(k, nums)[-1] 
'''
Get the largest k, and get the smallest (descending order) to get the k-th insteaf of the max.  Since the array isn't changing, no dynamic stuff needs to happen like with the stream
where we had to turn it into a heap (the nlargest function does it for us automatically, yay). Then, we had to get the top k elements in the heap and keep popping the minimum until it remains k largest because we kept having new ones come in and constantly running  nlargest would require copious amounts of time repeating for every add (m), so like m *nlog(k) time, 
so we had to only use the o(1) time stuff like push & pop

Much more understandable and articulated version:
For a static array, I can use `heapq.nlargest(k, nums)[-1]`. This gets the `k` largest elements in descending order, and the last element is the kth largest. Since the array isn't changing, I only need to perform this operation once.

`heapq.nlargest()` handles the heap operations internally, so I don't need to manually call `heapify()`.

For the stream version, however, new values are continuously added. I maintain a min-heap containing only the `k` largest elements seen so far. The minimum element of this heap is the kth largest.

Whenever a new value arrives, I push it into the heap. If the heap grows beyond `k` elements, I pop the minimum. This removes the smallest element from our current top-k and keeps the heap containing exactly the `k` largest elements.

This is more efficient than repeatedly calling `nlargest()` on the entire stream after every new value, because we only update the small heap instead of repeatedly processing the growing collection.
'''