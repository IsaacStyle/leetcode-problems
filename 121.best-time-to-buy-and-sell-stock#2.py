def maxProfit(self, prices):
        largest, min_price = 0,float('inf')
        for price in prices:
            min_price = min(min_price, price)
            profit = price - min_price
            largest = max(profit, largest)
        return largest