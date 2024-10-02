def max_profit(prices):
    if not prices:
        return 0
    
    min_price = prices[0]
    max_profit = 0
    
    for price in prices:
        min_price = min(min_price, price)
        max_profit = max(max_profit, price - min_price)
        
    return max_profit

user_input = input("Enter stock prices separated by spaces: ")
prices = list(map(int, user_input.split()))
result = max_profit(prices)
print("Maximum profit:", result)
