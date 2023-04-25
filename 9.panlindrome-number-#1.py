def isPalindrome(self, x):
        if x < 0: return False
        y = str(x)
        if y == y[::-1]: return True