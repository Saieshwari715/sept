class Solution:
    def addStrings(self, num1: str, num2: str) -> str:
        c=0
        r=[]
        i,j=len(num1)-1,len(num2)-1
        while i>=0 or j>=0 or c:
            x1=int(num1[i]) if i>=0 else 0
            x2=int(num2[j]) if j>=0 else 0
            t=x1+x2+c
            c=t//10
            r.append(str(t%10))
            i-=1
            j-=1
        return ''.join(r[::-1])

