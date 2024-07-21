import os
import pandas as pd
import time
from influxdb_client import InfluxDBClient, Point, WritePrecision
from influxdb_client.client.write_api import SYNCHRONOUS

# InfluxDB settings
token = 'MlUmh8wWKDAcBiZbBjvJPguGKxoON1ZRqFjVQ_zh8M3NHLcr53WnxbfXX_ByD0Wm7S8G0kb622gj2EX25MzFCA=='
org = "Portfolio_Opt"
url = "http://localhost:8080"
bucket = "Nifty50"

client = InfluxDBClient(url=url, token=token, org=org)
file_path='/Users/uddashyakumar/Downloads/NSEI.csv'
write_api = client.write_api(write_options=SYNCHRONOUS)
data = pd.read_csv(file_path)  # Or try 'cp1252' if 'ISO-8859-1' doesn't work
        # print(data)
        
for index, row in data.iterrows():
    print(f"Data from {file_path}  at {index} written to InfluxDB.", end="\r")
    point = (
        Point("market_data")
        .tag("symbol", 'NIFTY50')
        .field("open", float(row['Open']))
        .field("high", float(row['High']))
        .field("low", float(row['Low']))
        .field("close", float(row['Close']))
        .time(pd.to_datetime(row['Date']), WritePrecision.NS)
    )
    # Write the point to the InfluxDB
    write_api.write(bucket=bucket, org=org, record=point)
