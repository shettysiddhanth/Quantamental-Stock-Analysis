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
write_api = client.write_api(write_options=SYNCHRONOUS)

# Directory containing the CSV files
folder_path = '/Volumes/rog-phone5/NF_200/Nifty200_1h'
nifty50_symbols = [
    "ADANIENT",  # Adani Enterprises Ltd.
    "ADANIPORTS",  # Adani Ports and SEZ Ltd.
    "APOLLOHOSP",  # Apollo Hospitals Enterprise Ltd.
    "ASIANPAINT",  # Asian Paints Ltd.
    "AXISBANK",  # Axis Bank Ltd.
    "BAJAJ-AUTO",  # Bajaj Auto Ltd.
    "BAJFINANCE",  # Bajaj Finance Ltd.
    "BAJAJFINSV",  # Bajaj Finserv Ltd.
    "BHARTIARTL",  # Bharti Airtel Ltd.
    "BPCL",  # Bharat Petroleum Corporation Ltd.
    "BRITANNIA",  # Britannia Industries Ltd.
    "CIPLA",  # Cipla Ltd.
    "COALINDIA",  # Coal India Ltd.
    "DIVISLAB",  # Divi's Laboratories Ltd.
    "DRREDDY",  # Dr. Reddy's Laboratories Ltd.
    "EICHERMOT",  # Eicher Motors Ltd.
    "GRASIM",  # Grasim Industries Ltd.
    "HCLTECH",  # HCL Technologies Ltd.
    "HDFCBANK",  # HDFC Bank Ltd.
    "HDFCLIFE",  # HDFC Life Insurance Company Ltd.
    "HEROMOTOCO",  # Hero MotoCorp Ltd.
    "HINDALCO",  # Hindalco Industries Ltd.
    "HINDUNILVR",  # Hindustan Unilever Ltd.
    "HDFC",  # Housing Development Finance Corporation Ltd.
    "ICICIBANK",  # ICICI Bank Ltd.
    "ITC",  # ITC Ltd.
    "IOC",  # Indian Oil Corporation Ltd.
    "INDUSINDBK",  # IndusInd Bank Ltd.
    "INFY",  # Infosys Ltd.
    "JSWSTEEL",  # JSW Steel Ltd.
    "KOTAKBANK",  # Kotak Mahindra Bank Ltd.
    "LT",  # Larsen & Toubro Ltd.
    "M&M",  # Mahindra & Mahindra Ltd.
    "MARUTI",  # Maruti Suzuki India Ltd.
    "NESTLEIND",  # Nestle India Ltd.
    "NTPC",  # NTPC Ltd.
    "ONGC",  # Oil and Natural Gas Corporation Ltd.
    "POWERGRID",  # Power Grid Corporation of India Ltd.
    "RELIANCE",  # Reliance Industries Ltd.
    "SBILIFE",  # SBI Life Insurance Company Ltd.
    "SHREECEM",  # Shree Cement Ltd.
    "SBIN",  # State Bank of India
    "SUNPHARMA",  # Sun Pharmaceutical Industries Ltd.
    "TCS",  # Tata Consultancy Services Ltd.
    "TATACONSUM",  # Tata Consumer Products Ltd.
    "TATAMOTORS",  # Tata Motors Ltd.
    "TATASTEEL",  # Tata Steel Ltd.
    "TECHM",  # Tech Mahindra Ltd.
    "TITAN",  # Titan Company Ltd.
    "ULTRACEMCO"  # UltraTech Cement Ltd.
]


# Iterate through each file in the directory
for filename in os.listdir(folder_path):
    if filename.endswith('.csv'):
        file_path = os.path.join(folder_path, filename)
        
        # Read the CSV file
        # data = pd.read_csv(file_path)
        data = pd.read_csv(file_path, encoding='ISO-8859-1')  # Or try 'cp1252' if 'ISO-8859-1' doesn't work
        # print(data)
        
        for index, row in data.iterrows():
            if row["symbol"] in nifty50_symbols:
                print(f"Data from {filename}  at {index} written to InfluxDB.", end="\r")
                # Create a point with the data
                point = (
                    Point("market_data")
                    .tag("symbol", row['symbol'])
                    .field("open", float(row['open']))
                    .field("high", float(row['high']))
                    .field("low", float(row['low']))
                    .field("close", float(row['close']))
                    .field("volume", int(row['volume']))
                    .time(pd.to_datetime(row['datetime']), WritePrecision.NS)
                )
                # Write the point to the InfluxDB
                write_api.write(bucket=bucket, org=org, record=point)

