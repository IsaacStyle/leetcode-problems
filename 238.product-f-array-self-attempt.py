def productExceptSelf(self, nums):
        product = 1
        zero_count = 0
        result = []
        for i in nums:
            if i != 0:
                product *= i
            else: 
                zero_count += 1

        if zero_count > 1: return [0 for i in range(len(nums))]

        for i in nums:
            if i != 0 and zero_count == 1:
                result.append(0)
            elif i != 0:
                result.append(product * (float(1/i)))
                print 
            else:
                result.append(product)
        return result