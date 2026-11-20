import csv
from datetime import datetime

STOCK_PRICES = {
    "AAPL": 180.0,
    "TSLA": 250.0,
    "GOOGL": 140.0,
    "MSFT": 410.0,
    "AMZN": 175.0,
}


def save_report(portfolio_items, total_value):
  choice = (
      input("\nDo you want to save the portfolio report? (txt/csv/no): ")
      .strip()
      .lower()
  )
  timestamp = datetime.now().strftime("%Y%m%d_%H%M%S")

  if choice == "txt":
    filename = f"portfolio_{timestamp}.txt"
    with open(filename, "w", encoding="utf-8") as file:
      file.write("Stock Portfolio Summary\n")
      file.write("=" * 40 + "\n")
      for item in portfolio_items:
        file.write(
            f"{item['symbol']} | Qty: {item['quantity']} | "
            f"Price: ${item['price']:.2f} | Subtotal: ${item['subtotal']:.2f}\n"
        )
      file.write("=" * 40 + "\n")
      file.write(f"Total Investment Value: ${total_value:.2f}\n")
    print(f"Report saved to {filename}")

  elif choice == "csv":
    filename = f"portfolio_{timestamp}.csv"
    with open(filename, "w", newline="", encoding="utf-8") as file:
      writer = csv.DictWriter(
          file, fieldnames=["symbol", "quantity", "price", "subtotal"]
      )
      writer.writeheader()
      writer.writerows(portfolio_items)
      writer.writerow({"symbol": "TOTAL", "subtotal": round(total_value, 2)})
    print(f"Report saved to {filename}")

  else:
    print("Report not saved.")


def run_portfolio_tracker():
  print("=== Stock Portfolio Tracker ===")
  print("Available stocks and prices:")
  for symbol, price in STOCK_PRICES.items():
    print(f"  {symbol}: ${price:.2f}")
  print("Type 'done' as the stock name when finished.\n")

  portfolio_items = []
  total_value = 0.0

  while True:
    symbol = input("Enter stock symbol: ").strip().upper()
    if symbol == "DONE":
      break

    if symbol not in STOCK_PRICES:
      print(
          f"'{symbol}' is not in the price list. Choose from:"
          f" {', '.join(STOCK_PRICES.keys())}\n"
      )
      continue

    try:
      quantity = int(input(f"Enter quantity for {symbol}: ").strip())
      if quantity <= 0:
        print("Quantity must be greater than 0.\n")
        continue
    except ValueError:
      print("Please enter a valid whole number for quantity.\n")
      continue

    price = STOCK_PRICES[symbol]
    subtotal = price * quantity
    total_value += subtotal

    portfolio_items.append({
        "symbol": symbol,
        "quantity": quantity,
        "price": price,
        "subtotal": subtotal,
    })
    print(f"Added {quantity} x {symbol} (${subtotal:.2f})\n")

  if not portfolio_items:
    print("No stocks were added to your portfolio.")
    return

  print("\n--- Portfolio Summary ---")
  for item in portfolio_items:
    print(
        f"{item['symbol']:<6} | Qty: {item['quantity']:<4} | "
        f"Price: ${item['price']:>7.2f} | Value: ${item['subtotal']:>8.2f}"
    )
  print("-" * 48)
  print(f"Total Investment Value: ${total_value:.2f}")

  save_report(portfolio_items, total_value)


if __name__ == "__main__":
  run_portfolio_tracker()
