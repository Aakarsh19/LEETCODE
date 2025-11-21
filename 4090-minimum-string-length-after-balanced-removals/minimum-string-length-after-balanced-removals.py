class Solution:
    def minLengthAfterRemovals(self, s: str) -> int:
        ac = s.count('a')
        bc = s.count('b')
        return abs(ac-bc)