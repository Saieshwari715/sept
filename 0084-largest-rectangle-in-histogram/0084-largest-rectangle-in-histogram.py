class Solution:
    def largestRectangleArea(self, heights: List[int]) -> int:
        s=[]
        maxi=0
        for i,h in enumerate(heights):
            strt=i
            while s and s[-1][1]>h:
                idx,h1=s.pop()
                maxi=max(maxi,h1*(i-idx))
                strt=idx
            s.append((strt,h))
            n=len(heights)
        for idx,h1 in s:
            maxi=max(maxi,h1*(n-idx))
        return maxi
        
        