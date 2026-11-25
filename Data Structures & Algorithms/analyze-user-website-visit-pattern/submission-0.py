from collections import defaultdict
class Solution:
    def mostVisitedPattern(self, username: List[str], timestamp: List[int], website: List[str]) -> List[str]:
        event_list = [(user,time,site) for user, time, site in zip(username, timestamp, website)]
        event_list.sort() 
         
        patterns = defaultdict(set)
        #I was thinking of making a new hashmap of user -> pattern but that adds an extra o(n) time loop
        for index, event in enumerate(event_list):
            first_user = event_list[index][0]
            first_site = event_list[index][2]
            
            for index2 in range(index + 1, len(event_list)):
                second_user = event_list[index2][0]
                second_site = event_list[index2][2]
                if second_user != first_user: continue
                
                for index3 in range(index2 + 1, len(event_list)):
                    third_user = event_list[index3][0]
                    third_site = event_list[index3][2]
                    if third_user != first_user: continue
                    
                    patterns[(first_site,second_site,third_site)].add(first_user)


       
            
        #3. Check each pattern's person amount and return the one with the smallest 
        #lexograph
        most_visited_pattern = (0, None)
        for pattern, users in patterns.items(): most_visited_pattern = min(most_visited_pattern, (-len(users),pattern))
        #Return
        return list(most_visited_pattern[1])