# NUMBER OF COMMON FACTOR
class Solution:
    def commonFactors(self, a: int, b: int) -> int:
        p=[]
        s=[]
        c=0
        for i in range(1,a+1):
            if a%i==0:
                p.append(i)
        for j in range(1,b+1):
            if b%j==0:
                s.append(j)
        s=set(s)
        p=set(p)
        
        return len(p.intersection(s))


