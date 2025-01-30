import yfinance as yf
import csv
import time

# Define tickers and their corresponding sectors
tickers_sectors = {
    "AAPL": "Technology", "MSFT": "Technology", "GOOGL": "Technology", "AMZN": "Technology", "META": "Technology",
    "JNJ": "Healthcare", "PFE": "Healthcare", "MRNA": "Healthcare", "UNH": "Healthcare", "CVS": "Healthcare",
    "JPM": "Finance", "GS": "Finance", "BAC": "Finance", "C": "Finance", "WFC": "Finance",
    "XOM": "Energy", "CVX": "Energy", "BP": "Energy", "TTE": "Energy", "PSX": "Energy",
    "TSLA": "Automotive", "F": "Automotive", "GM": "Automotive", "HMC": "Automotive", "TM": "Automotive",
    "PG": "Consumer Goods", "KO": "Consumer Goods", "PEP": "Consumer Goods", "UL": "Consumer Goods", "CL": "Consumer Goods",
    "WMT": "Retail", "TGT": "Retail", "COST": "Retail", "BBY": "Retail", "M": "Retail",
    "VZ": "Telecommunications", "T": "Telecommunications", "TMUS": "Telecommunications", "CHTR": "Telecommunications", "CMCSA": "Telecommunications",
    "BA": "Aerospace & Defense", "LMT": "Aerospace & Defense", "NOC": "Aerospace & Defense", "RTX": "Aerospace & Defense", "GD": "Aerospace & Defense",
    "MMM": "Industrial", "CAT": "Industrial", "DE": "Industrial", "GE": "Industrial", "HON": "Industrial",
    "NSRGY": "Food & Beverage", "MDLZ": "Food & Beverage", "KHC": "Food & Beverage", "HRL": "Food & Beverage", "SJM": "Food & Beverage",
    "UPS": "Transportation", "FDX": "Transportation", "CSX": "Transportation", "NSC": "Transportation", "UNP": "Transportation",
    "NEE": "Utilities", "DUK": "Utilities", "D": "Utilities", "AEP": "Utilities", "SO": "Utilities"
}

# CSV file setup
csv_filename = "stock_data_2024_1_month.csv"
header = ["Date", "Ticker", "Sector", "Open", "High", "Low", "Close", "Volume"]

# Open CSV file for writing
with open(csv_filename, mode="w", newline="") as file:
    writer = csv.writer(file)
    writer.writerow(header)  # Write column headers

    # Loop through each ticker and fetch data
    for ticker, sector in tickers_sectors.items():
        try:
            stock = yf.Ticker(ticker)
            
            # Fetch data for 2024
            hist = stock.history(start="2024-12-01", end="2025-01-01")

            for date, row in hist.iterrows():
                writer.writerow([
                    date.strftime('%Y-%m-%d'), ticker, sector,
                    row["Open"], row["High"], row["Low"], row["Close"], row["Volume"]
                ])
            print(f"Data retrieved for {ticker}")

        except Exception as e:
            print(f"Error retrieving data for {ticker}: {e}")

        # Add a small delay to prevent rate-limiting issues
        time.sleep(1)

print(f"Data saved to {csv_filename}")
