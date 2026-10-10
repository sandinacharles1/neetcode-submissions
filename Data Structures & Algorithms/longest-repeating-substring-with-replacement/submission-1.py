class Solution:
    def characterReplacement(self, s: str, k: int) -> int:
        char_counts = dict()
        max_window_len = 0
        left_idx = 0
        max_frequency = 0
        
        for right_idx, right_val in enumerate(s):
            char_counts[right_val] = char_counts.get(right_val, 0) + 1
            replacement_count = sum(char_counts.values()) - max(char_counts.values())
            
            while replacement_count > k:
                left_val = s[left_idx]
                char_counts[left_val] = char_counts.get(left_val, 0) - 1
                left_idx += 1
                replacement_count = sum(char_counts.values()) - max(char_counts.values())

            
            max_window_len = max(max_window_len, right_idx - left_idx + 1)
        
        return max_window_len