class Solution:
    def containsNearbyDuplicate(self, nums: List[int], k: int) -> bool:
        n=len(nums)

        seen={}
        found=False
        for i in range(n):
            if nums[i] in seen and i-seen[nums[i]]<=k:
                return True
                found=True
                break
            seen[nums[i]]=i
        if not found:
            return False


        