class Solution:
    def majorityElement(self, nums: List[int]) -> List[int]:
        num_frequency = Counter(nums)
        num_frequency = [(-frequency, num) for num,frequency in num_frequency.items()]
        heapq.heapify(num_frequency)
        
        output = []
        while num_frequency:
            frequency, number = heapq.heappop(num_frequency)
            if abs(frequency) <= len(nums) / 3:
                break
            output.append(number)
        return output