#pip install yfinance

import yfinance as yf

# Definir los tickers
tickers = ["AMZN", "TSLA", "NVDA"]
dates = ["1997-05-15", "2010-06-29", "1999-01-22"]

# Descargar datos históricos
for i in range(0,3):
    data = yf.download(tickers[i], start=dates[i], end="2025-05-01")  # Ajusta las fechas según necesites
    data.to_csv(f"DATA/{tickers[i]}_historical_data.csv")  # Guardar en archivo CSV

print("Descarga completa")