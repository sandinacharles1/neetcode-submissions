class TimeMap:

    def __init__(self):
        self.time_map = dict()
        '''
        { timestamp:
            {key: value,
            key1: value1,}
        }
        '''

    def set(self, key: str, value: str, timestamp: int) -> None:
        self.time_map.setdefault(timestamp, {})[key] = value

    def get(self, key: str, timestamp: int) -> str:
        while timestamp >= 0:
            if timestamp not in self.time_map:
                timestamp -= 1
                continue 
            
            if key in self.time_map[timestamp]:
                return f"{self.time_map[timestamp][key]}"
            
            timestamp -= 1
        return ""

        
