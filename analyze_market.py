import pandas as pd

def analyze_market():
    # Read data from CSV
    try:
        data = pd.read_csv("stock_data.csv")
    except FileNotFoundError:
        print("Error: 'stock_data.csv' not found.")
        return

    # Ensure required columns exist
    if 'Date' not in data.columns or 'Price' not in data.columns:
        print("Error: Required columns 'Date' and 'Price' are missing in the CSV file.")
        return

    # Convert Date column to datetime
    data['Date'] = pd.to_datetime(data['Date'])

    # Sort data by Date
    data = data.sort_values(by='Date')

    # Calculate overall trend (using the average price across all stocks per day)
    daily_avg = data.groupby('Date')['Price'].mean().reset_index()
    
    start_price = daily_avg['Price'].iloc[0]
    end_price = daily_avg['Price'].iloc[-1]
    trend = "upward" if end_price > start_price else "downward" if end_price < start_price else "stable"

    # average closing price
    avg_price = data['Price'].mean()

    # Save analysis results
    with open("market_analysis.txt", "w") as file:
        file.write("Market Analysis Report\n")
        file.write("======================\n")
        file.write(f"Overall Trend: {trend}\n")
        file.write(f"Starting Price: {start_price:.2f}\n")
        file.write(f"Ending Price: {end_price:.2f}\n")
        file.write(f"Average Closing Price: {avg_price:.2f}\n")

    print("Market analysis completed and saved to 'market_analysis.txt'.")

if __name__ == "__main__":
    analyze_market()
