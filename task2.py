stock_prices = {
    "AAPL": 180,
    "TSLA": 250,
    "GOOGL": 2700,
    "MSFT": 310,
    "AMZN": 3300
}

portfolio = {}

while True:
    stock = input("Enter stock symbol (AAPL, TSLA, etc.) or type 'done' to finish: ").upper()
    if stock == "DONE":
        break
    if stock not in stock_prices:
        print("Stock not found in database.")
        continue

    try:
        quantity = int(input(f"Enter quantity of {stock}: "))
        portfolio[stock] = portfolio.get(stock, 0) + quantity
    except ValueError:
        print("Invalid quantity. Please enter a number.")

total_value = 0
print("\nYour Portfolio:")
for stock, quantity in portfolio.items():
    price = stock_prices[stock]
    investment = price * quantity
    total_value += investment
    print(f"{stock}: {quantity} shares × ${price} = ${investment}")

print(f"\nTotal Investment: ${total_value}")

save_option = input("Do you want to save this portfolio to 'portfolio.txt'? (yes/no): ").lower()
if save_option == 'yes':
    with open("portfolio.txt", "w") as file:
        file.write("Stock Portfolio:\n")
        for stock, quantity in portfolio.items():
            price = stock_prices[stock]
            investment = price * quantity
            file.write(f"{stock}: {quantity} shares × ${price} = ${investment}\n")
        file.write(f"\nTotal Investment: ${total_value}\n")
    print("Portfolio saved to 'portfolio.txt'")
