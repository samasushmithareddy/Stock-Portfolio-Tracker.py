# Task 2# Task 2: Stock Portfolio Tracker

def stock_tracker():
    # 1. Hardcoded dictionary to define stock prices
    stock_prices = {
        "AAPL": 180,
        "TSLA": 250,
        "GOOGL": 150,
        "MSFT": 400,
        "AMZN": 175
    }
    
    portfolio = {}
    
    print("--- CodeAlpha Stock Portfolio Tracker ---")
    print(f"Available Stocks: {', '.join(stock_prices.keys())}")
    
    # 2. User inputs stock names and quantity
    while True:
        symbol = input("\nEnter stock symbol to add (or type 'done' to finish): ").upper()
        
        if symbol == 'DONE':
            break
        
        if symbol in stock_prices:
            try:
                quantity = int(input(f"How many shares of {symbol} do you own? "))
                portfolio[symbol] = quantity
            except ValueError:
                print("Please enter a valid number for quantity.")
        else:
            print("Stock not found in our database. Please choose from the list above.")

    # 3. Calculate and display total investment value
    print("\n--- Your Portfolio Summary ---")
    total_value = 0
    
    for stock, qty in portfolio.items():
        price = stock_prices[stock]
        value = qty * price
        total_value += value
        print(f"{stock}: {qty} shares @ ${price} = ${value}")
    
    print("-" * 30)
    print(f"TOTAL INVESTMENT VALUE: ${total_value}")

if __name__ == "__main__":
    stock_tracker()

def stock_tracker():
    # 1. Hardcoded dictionary to define stock prices
    stock_prices = {
        "AAPL": 180,
        "TSLA": 250,
        "GOOGL": 150,
        "MSFT": 400,
        "AMZN": 175
    }
    
    portfolio = {}
    
    print("--- CodeAlpha Stock Portfolio Tracker ---")
    print(f"Available Stocks: {', '.join(stock_prices.keys())}")
    
    # 2. User inputs stock names and quantity
    while True:
        symbol = input("\nEnter stock symbol to add (or type 'done' to finish): ").upper()
        
        if symbol == 'DONE':
            break
        
        if symbol in stock_prices:
            try:
                quantity = int(input(f"How many shares of {symbol} do you own? "))
                portfolio[symbol] = quantity
            except ValueError:
                print("Please enter a valid number for quantity.")
        else:
            print("Stock not found in our database. Please choose from the list above.")

    # 3. Calculate and display total investment value
    print("\n--- Your Portfolio Summary ---")
    total_value = 0
    
    for stock, qty in portfolio.items():
        price = stock_prices[stock]
        value = qty * price
        total_value += value
        print(f"{stock}: {qty} shares @ ${price} = ${value}")
    
    print("-" * 30)
    print(f"TOTAL INVESTMENT VALUE: ${total_value}")

if __name__ == "__main__":
    stock_tracker()
