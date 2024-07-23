import yfinance as yf
from influxdb_client import InfluxDBClient, Point, WritePrecision
from influxdb_client.client.write_api import SYNCHRONOUS
import pandas as pd
# InfluxDB settings
token = 'MlUmh8wWKDAcBiZbBjvJPguGKxoON1ZRqFjVQ_zh8M3NHLcr53WnxbfXX_ByD0Wm7S8G0kb622gj2EX25MzFCA=='
org = "Portfolio_Opt"
url = "http://localhost:8080"
bucket = "Nifty50"

client = InfluxDBClient(url=url, token=token, org=org)
write_api = client.write_api(write_options=SYNCHRONOUS)

nifty50_symbols = [
    "ADANIENT.NS", "ADANIPORTS.NS", "APOLLOHOSP.NS", "ASIANPAINT.NS",
    "AXISBANK.NS", "BAJAJ-AUTO.NS", "BAJFINANCE.NS", "BAJAJFINSV.NS",
    "BHARTIARTL.NS", "BPCL.NS", "BRITANNIA.NS", "CIPLA.NS", "COALINDIA.NS",
    "DIVISLAB.NS", "DRREDDY.NS", "EICHERMOT.NS", "GRASIM.NS", "HCLTECH.NS",
    "HDFCBANK.NS", "HDFCLIFE.NS", "HEROMOTOCO.NS", "HINDALCO.NS",
    "HINDUNILVR.NS", "HDFCBANK.NS", "ICICIBANK.NS", "ITC.NS", "IOC.NS",
    "INDUSINDBK.NS", "INFY.NS", "JSWSTEEL.NS", "KOTAKBANK.NS", "LT.NS",
    "M&M.NS", "MARUTI.NS", "NESTLEIND.NS", "NTPC.NS", "ONGC.NS",
    "POWERGRID.NS", "RELIANCE.NS", "SBILIFE.NS", "SHREECEM.NS", "SBIN.NS",
    "SUNPHARMA.NS", "TCS.NS", "TATACONSUM.NS", "TATAMOTORS.NS",
    "TATASTEEL.NS", "TECHM.NS", "TITAN.NS", "ULTRACEMCO.NS"
]

# Fetch and write data
for symbol in nifty50_symbols:
    data = yf.download(symbol, start="2017-01-01", end=pd.Timestamp.today().strftime('%Y-%m-%d')  , progress=False)
    for index, row in data.iterrows():
        point = (
            Point("market_data")
            .tag("symbol", symbol)
            .field("open", float(row['Open']))
            .field("high", float(row['High']))
            .field("low", float(row['Low']))
            .field("close", float(row['Close']))
            .field("volume", int(row['Volume']))
            .time(index, WritePrecision.NS)
        )
        write_api.write(bucket=bucket, org=org, record=point)
        print(f"Data for {symbol} on {index.date()} written to InfluxDB.", end="\r")

print("All data written to InfluxDB.")
