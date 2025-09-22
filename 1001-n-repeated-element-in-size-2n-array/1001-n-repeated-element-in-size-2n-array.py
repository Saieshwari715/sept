class Solution:
    def repeatedNTimes(self, nums: List[int]) -> int:
        hash = {}
        for num in nums:
            if num in hash:
                hash[num] += 1
                if hash[num] == 2:
                    return num
            else:
                hash[num] = 1


        