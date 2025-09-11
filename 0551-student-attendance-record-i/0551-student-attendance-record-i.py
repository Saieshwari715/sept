class Solution:
    def checkRecord(self, s: str) -> bool:
        for char in s:
            c=s.count("A")
            if(c<2 and "LLL" not in s):
                return True
        return False