class Solution:
    def minLengthAfterRemovals(self, s: str) -> int:
        ac = s.count('a')
        bc = s.count('b')
        x = abs(ac-bc)
        return x