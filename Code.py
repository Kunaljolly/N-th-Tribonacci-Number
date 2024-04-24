class Solution:
    def tribonacci(self, n: int) -> int:
        
        if n == 0:
            return 0
        if n == 1:
            return 1
        if n == 2:
            return 1
        x = 3
        t = []
        t.append(0)
        t.append(1)
        t.append(1)

        while(x != n+1):
            t.append(t[x-1]+t[x-2]+t[x-3])
            x += 1
        return t[-1]

