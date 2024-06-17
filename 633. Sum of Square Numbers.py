class Solution:
    def judgeSquareSum(self, c: int) -> bool:
        b = math.floor(math.sqrt(c))
        a = 1
        if (b*b == c):
            return True
        while a <= b:
            val = (a*a) + (b*b)
            if val < c:
                a = a + 1
            elif val > c:
                b = b - 1
            else:
                return True

        return False

        
