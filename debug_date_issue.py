import yfinance as yf
import pandas as pd

# Replicate your issue
df_wpm = yf.Ticker('WPM').history(start='2022-03-28', end='2026-03-28', interval='1d')
print("Original Date column:")
print(df_wpm['Date'].head() if 'Date' in df_wpm.columns else df_wpm.index[:5])
print("\nDate dtype:")
print(df_wpm.index.dtype)

# Your current approach
df_wpm_reset = df_wpm.reset_index()
print("\nAfter reset_index:")
print(df_wpm_reset['Date'].head())
print("Date dtype:", df_wpm_reset['Date'].dtype)

# The issue is likely here - let's see what happens when we convert to string
df_wpm_reset['date'] = df_wpm_reset['Date'].dt.strftime('%Y-%m-%d')
print("\nAfter strftime conversion:")
print(df_wpm_reset['date'].head())
print("Date dtype:", df_wpm_reset['date'].dtype)

# Better approach - convert to datetime without timezone
df_wpm_reset['date_fixed'] = pd.to_datetime(df_wpm_reset['Date'].dt.date)
print("\nAfter fixing with dt.date:")
print(df_wpm_reset['date_fixed'].head())
print("Date dtype:", df_wpm_reset['date_fixed'].dtype)