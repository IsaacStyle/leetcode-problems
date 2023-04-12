def maxProfit(self, prices):
        largest = 0
        map = {}
        for i,price in enumerate(prices):
            for item in map:
                if price - map[item] > largest:
                    largest = price - map[item]
            map[price] = price
        return largest