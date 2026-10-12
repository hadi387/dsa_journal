def max_profit(prices):
    min_price = prices[0]
    max_profit = 0

    for price in prices:
        if price < min_price:
            min_price = price

        possible_profit = price - min_price

        if possible_profit > max_profit:
            max_profit = possible_profit

    return max_profit

print(max_profit([7, 1, 5, 3, 6, 4]))
