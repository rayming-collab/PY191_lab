# -*- coding: utf-8 -*-
"""
Corrected code to download stock data using yfinance.
"""

import os
import pandas as pd
import numpy as np
import yfinance as yf
import matplotlib.pyplot as plt

def get_stock(ticker, start_date, end_date, s_window, l_window):
    """Retrieve stock data and compute indicators."""
    try:
        # Download stock data
        df = yf.download(ticker, start=start_date, end=end_date)
        if df.empty:
            print(f"No data found for {ticker}")
            return None

        # Calculate daily returns
        df['Return'] = df['Close'].pct_change().fillna(0)

        # Process date attributes
        df.reset_index(inplace=True)
        df['Date'] = pd.to_datetime(df['Date'])
        df['Year'] = df['Date'].dt.year
        df['Month'] = df['Date'].dt.month
        df['Day'] = df['Date'].dt.day
        df['Weekday'] = df['Date'].dt.day_name()
        df['Week_Number'] = df['Date'].dt.strftime('%U')
        df['Year_Week'] = df['Date'].dt.strftime('%Y-%U')

        # Round price columns
        price_cols = ['Open', 'High', 'Low', 'Close']
        df[price_cols] = df[price_cols].round(2)

        # Calculate moving averages
        df['Short_MA'] = df['Close'].rolling(window=s_window, min_periods=1).mean()
        df['Long_MA'] = df['Close'].rolling(window=l_window, min_periods=1).mean()

        # Reorder columns
        col_order = [
            'Date', 'Year', 'Month', 'Day', 'Weekday', 'Week_Number', 'Year_Week',
            'Open', 'High', 'Low', 'Close', 'Volume', 'Return',
            'Short_MA', 'Long_MA'
        ]

        return df[col_order]

    except Exception as e:
        print(f"Error processing {ticker}: {str(e)}")
        return None

# Example usage
if __name__ == "__main__":
    try:
        ticker = "PG"
        output_file = os.path.join(os.getcwd(), f"{ticker}.csv")

        # Get stock data
        df = get_stock(
            ticker=ticker,
            start_date="2021-01-01",
            end_date="2025-12-31",
            s_window=14,
            l_window=50
        )

        fig, ax = plt.subplots(figsize=(10, 5))
        
        # Plot multiple data lines against the Date column
        ax.plot(df['Date'], df['Close'], label='Close Price', color='black')
        
        # Chart Styling
        ax.set_title(f"{ticker} Close Price Over Time", fontsize=14)
        ax.set_xlabel("Date", fontsize=12)
        ax.set_ylabel("Value", fontsize=12)
    
        plt.show()

        averages = (
            df.groupby("Weekday")["Return"]
            .mean()
        )
        print(averages)

        count = np.zeros(10)
        for i in range(len(df)):
            number = 100 * df.loc[i, ("Close", ticker)]
            last_digit = int(number % 10)
            count[last_digit] += 1
        count = count / count.sum()
        for i in range (len(count)):
            print("Percentage of digit", i, ":", count[i] * 100, "%")
        

        
        # Save to CSV if data exists
        if df is not None:
            df.drop(index=1, inplace=True) 
            df.to_csv(output_file, index=False)
            print(f"Successfully saved {len(df)} records to {output_file}")
        else:
            print("No data available to save.")

    except Exception as e:
        print(f"Main execution error: {str(e)}")