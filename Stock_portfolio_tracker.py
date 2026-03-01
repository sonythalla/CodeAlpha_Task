# Simple Stock Portfolio Tracker

# File to store portfolio data
portfolio_file = "portfolio.txt"

# Load existing portfolio from file
def load_portfolio():
    portfolio = {}
    try:
        with open(portfolio_file, "r") as f:
            for line in f:
                line = line.strip()
                if line:
                    ticker, shares, price = line.split(",")
                    portfolio[ticker] = [int(shares), float(price)]
    except FileNotFoundError:
        pass
    return portfolio

# Save portfolio to file
def save_portfolio(portfolio):
    with open(portfolio_file, "w") as f:
        for ticker, (shares, price) in portfolio.items():
            f.write(f"{ticker},{shares},{price}\n")

# Display portfolio
def display_portfolio(portfolio):
    total_value = sum(shares * price for shares, price in portfolio.values())
    print("\nPortfolio Summary")
    print("-" * 40)
    for ticker, (shares, price) in portfolio.items():
        value = shares * price
        percent = (value / total_value * 100) if total_value else 0
        print(f"{ticker}: {shares} × ${price:.2f} = ${value:.2f} ({percent:.1f}%)")
    print("-" * 40)
    print(f"Total Portfolio Value: ${total_value:.2f}\n")

# Add or update stock
def add_stock(portfolio):
    ticker = input("Enter stock ticker: ").upper()
    shares = int(input("Enter number of shares: "))
    price = float(input("Enter price per share: "))
    if ticker in portfolio:
        portfolio[ticker][0] += shares  # Add shares
        portfolio[ticker][1] = price    # Update price
    else:
        portfolio[ticker] = [shares, price]
    print(f"{ticker} added/updated successfully.")

# Remove stock
def remove_stock(portfolio):
    ticker = input("Enter stock ticker to remove: ").upper()
    if ticker in portfolio:
        portfolio.pop(ticker)
        print(f"{ticker} removed from portfolio.")
    else:
        print(f"{ticker} not found.")

# Main program
def main():
    portfolio = load_portfolio()
    
    while True:
        print("\n--- Stock Portfolio Tracker ---")
        print("1. View Portfolio")
        print("2. Add/Update Stock")
        print("3. Remove Stock")
        print("4. Exit")
        choice = input("Choose an option (1-4): ")
        
        if choice == "1":
            display_portfolio(portfolio)
        elif choice == "2":
            add_stock(portfolio)
            save_portfolio(portfolio)
        elif choice == "3":
            remove_stock(portfolio)
            save_portfolio(portfolio)
        elif choice == "4":
            print("Exiting Portfolio Tracker. Goodbye!")
            break
        else:
            print("Invalid option. Please choose 1-4.")

# Run the tracker
if __name__ == "__main__":
    main()
