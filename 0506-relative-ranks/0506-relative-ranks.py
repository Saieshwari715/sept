class Solution:
    def findRelativeRanks(self, score: List[int]) -> List[str]:
        pairs=[]
        for i in range(len(score)):
            pairs.append((score[i],i))
            pairs.sort(reverse=True)
        result=[""]*len(score)
        for rank in range(len(pairs)):
            val,idx=pairs[rank]
            if rank==0:
                result[idx]="Gold Medal"
            elif rank == 1:
                result[idx] = "Silver Medal"
            elif rank == 2:
                result[idx] = "Bronze Medal"
            else:
                result[idx] = str(rank + 1)
        return result
            
        