# Initial portfolio: ticker -> shares
portfolio = {"AAPL": 10, "MSFT": 5, "GOOGL": 2}
# Stock prices: ticker -> price
prices = {"AAPL": 172.26, "MSFT": 310.10, "GOOGL": 135.50}

def display_portfolio(portfolio, prices):
    total = sum(shares * prices.get(ticker, 0) for ticker, shares in portfolio.items())
    print("\nPortfolio Summary:")
    print("-" * 40)
    for ticker, shares in portfolio.items():
        value = shares * prices.get(ticker, 0)
        percent = (value / total * 100) if total else 0
        print(f"{ticker}: {shares} × ${prices[ticker]} = ${value:.2f} ({percent:.1f}%)")
    print("-" * 40)
    print(f"Total Portfolio Value: ${total:.2f}\n")

def add_stock(portfolio, prices):
    ticker = input("Enter ticker to add: ").upper()
    shares = int(input("Enter number of shares: "))
    price = float(input("Enter price per share: "))
    portfolio[ticker] = portfolio.get(ticker, 0) + shares
    prices[ticker] = price
    print(f"{ticker} added/updated successfully.")

def remove_stock(portfolio):
    ticker = input("Enter ticker to remove: ").upper()
    if ticker in portfolio:
        portfolio.pop(ticker)
        print(f"{ticker} removed from portfolio.")
    else:
        print(f"{ticker} not found.")

def update_price(prices):
    ticker = input("Enter ticker to update price: ").upper()
    if ticker in prices:
        price = float(input("Enter new price: "))
        prices[ticker] = price
        print(f"{ticker} price updated to ${price}.")
    else:
        print(f"{ticker} not found in prices list.")

# Main interactive menu
while True:
    print("\n--- Portfolio Manager ---")
    print("1. View Portfolio")
    print("2. Add Stock")
    print("3. Remove Stock")
    print("4. Update Stock Price")
    print("5. Exit")
    choice = input("Choose an option (1-5): ")

    if choice == "1":
        display_portfolio(portfolio, prices)
    elif choice == "2":
        add_stock(portfolio, prices)
    elif choice == "3":
        remove_stock(portfolio)
    elif choice == "4":
        update_price(prices)
    elif choice == "5":
        print("Exiting Portfolio Manager. Goodbye!")
        break
    else:
        print("Invalid option. Please choose 1-5.")
