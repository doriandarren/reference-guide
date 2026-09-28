stock_prices = [100.0, 110.0, 95.0, 98.0]
stock_prices = [150.0, 149.4, 145.5, 134]

first_price_increased = stock_prices[0] + (stock_prices[0] * 0.10)
first_price_decreased = stock_prices[0] - (stock_prices[0] * 0.10) 

for i in range(1, len(stock_prices)):
    ##print(stock_prices[i])
    
    if stock_prices[i] >= first_price_increased:
        print(f"Alert: Stock has increased to {stock_prices[i]}, which is 10% or more than the first price!")
        break

    if stock_prices[i] <= first_price_decreased:
        print(f"Alert: Stock has decreased to {stock_prices[i]}, which is 10% or less than the first price!")
        break
