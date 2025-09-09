class Solution:
    def maximumGap(self, nums: List[int]) -> int:
        nums.sort()
        n=len(nums)
        maxi=0
        if(n<2):
            return 0
        else:
            for i in range(1,n):
                s=nums[i]-nums[i-1]
                maxi=max(maxi,s)
            return maxi
        