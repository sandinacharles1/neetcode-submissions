class Solution:
    def carFleet(self, target: int, position: List[int], speed: List[int]) -> int:
        sorted_position_speed_list = []
        num_of_fleets = 0
        for indiv_position, indiv_speed in zip(position, speed):
            time = (target - indiv_position) / indiv_speed
            sorted_position_speed_list.append((indiv_position, time, indiv_speed))
        
        sorted_position_speed_list.sort(reverse=False) 

        while sorted_position_speed_list:
            if len(sorted_position_speed_list) == 1: 
                num_of_fleets += 1
                break

            current_position, current_time, current_speed = sorted_position_speed_list.pop()
            future_position, future_time, future_speed = sorted_position_speed_list[-1]
            if future_time <= current_time:
                sorted_position_speed_list[-1] = (future_position, current_time, future_speed)
            else:
                
                num_of_fleets += 1
        
        return num_of_fleets
