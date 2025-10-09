class Solution:
    def trap(self, arr: List[int]) -> int:
        n=len(arr)
        lmax=rmax=w=0
        l=0
        r=n-1
        while l<r:
            if(arr[l]<arr[r]):
                w+=max(0,lmax-arr[l])
                lmax=(max(lmax,arr[l]))
                l+=1
            else:
                w+=max(0,rmax-arr[r])
                rmax=(max(rmax,arr[r]))
                r-=1
        return w
        
        