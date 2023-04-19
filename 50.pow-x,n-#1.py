def myPow(self, x, n):
        if n == 0: return 1        
        result = 1
        for i in range(abs(n)):
            result *= x
        return result if n > 0 else 1/result