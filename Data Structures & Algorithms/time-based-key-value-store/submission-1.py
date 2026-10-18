import bisect
class TimeMap:

    def __init__(self):
        self.time_map = dict()
        '''{ timestamp:
            {key: value,
            key1: value1,}
        }''' #O(timestamps * O(keys))

    def set(self, key: str, value: str, timestamp: int) -> None:
        self.time_map.setdefault(key, []).append((timestamp, value)) #O(1)

    def get(self, key: str, timestamp: int) -> str:
        #WE can store the key then look at their different timestamps to eassily find the timeestamp closest to before the given timestamp. we keep saving the most recent seen one just incase
        try:
            #Edge cases, time stamp out of range (too big (index error), too small)
            timestamp_list = self.time_map[key]
            if timestamp > timestamp_list[-1][0]:
                return timestamp_list[-1][1]
            elif timestamp < timestamp_list[0][0]:
                return ""
            
            index = bisect.bisect_left(timestamp_list, timestamp, key = lambda pair: pair[0])
            if timestamp_list[index][0] == timestamp:
                return timestamp_list[index][1]
            else:
                return timestamp_list[index - 1][1]
        
        except KeyError:
            return ""
