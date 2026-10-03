class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        s_hash = Counter(s)
        t_hash = Counter(t)
        return s_hash == t_hash