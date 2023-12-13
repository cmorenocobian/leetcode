'''
https://leetcode.com/problems/sqrtx
'''

class Solution:
    def mySqrt0(self, x: int) -> int:
        number=0
        while (number+1)**2<=x:
            number+=1
        return number
    
    def mySqrt(self, x: int) -> int:
        if x==0:
            return 0
        inf, sup= 1, x
        result = 0

        while inf<=sup:
            cent= inf + (sup-inf)//2
            if cent*cent<= x:
                result=cent
                inf = cent+1
            else:
                sup=cent-1
        return result