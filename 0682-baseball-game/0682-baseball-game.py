class Solution:
    def calPoints(self, operations: List[str]) -> int:
        a=[]
        for i in operations:
            if(i=='+'):
                a.append(a[-1]+a[-2])
            elif(i=='D'):
                a.append(2*a[-1])
            elif(i=='C'):
                a.pop()
            else:
                a.append(int(i))
        return sum(a)



        