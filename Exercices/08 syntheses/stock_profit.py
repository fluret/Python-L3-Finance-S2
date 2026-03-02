def stock_profit(stock: list) -> int:
    best_profit = 0
    min_price = stock[0]

    for price in stock[1:]:
        best_profit = max(best_profit, price - min_price)
        min_price = min(min_price, price)

    return best_profit