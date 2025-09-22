class Solution:
    def findTheDifference(self, s: str, t: str) -> str:
        s_s=sum(ord(i) for i in s)
        t_s=sum(ord(j) for j in t)
        e=t_s-s_s
        return chr(e)

