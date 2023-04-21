def myPow(self, x, n):
        m = abs(n)
        result = 1.0
        while m:
            if m & 1:
                result *= x
            x *= x
            m >>= 1
        return result if n >= 0 else 1/result