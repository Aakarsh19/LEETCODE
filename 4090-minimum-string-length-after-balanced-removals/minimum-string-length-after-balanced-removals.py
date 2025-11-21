class Solution:
    def minLengthAfterRemovals(self, s: str) -> int:
        s = list(s)
        ac = s.count('a')
        bc = s.count('b')
        x = abs(ac-bc)
        return x