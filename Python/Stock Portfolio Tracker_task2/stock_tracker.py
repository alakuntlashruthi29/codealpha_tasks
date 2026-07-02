stock_prices = {
    "AAPL": 180,
    "TSLA": 250,
    "GOOGL": 140,
    "MSFT": 320,
    "AMZN": 150
}
total = 0
n = int(input("How many stocks do you want to enter? "))
for i in range(n):
    stock = input("Enter Stock Name: ").upper()
    quantity = int(input("Enter Quantity: "))
    if stock in stock_prices:
        price = stock_prices[stock]
        investment = price * quantity
        total += investment
        print("Investment for", stock, "=", investment)
    else:
        print("Stock not found")

print("\nTotal Investment =", total)