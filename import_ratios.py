# import pandas as pd
# from influxdb_client import InfluxDBClient, Point, WritePrecision
# from influxdb_client.client.write_api import SYNCHRONOUS

# # InfluxDB settings
# token = 'MlUmh8wWKDAcBiZbBjvJPguGKxoON1ZRqFjVQ_zh8M3NHLcr53WnxbfXX_ByD0Wm7S8G0kb622gj2EX25MzFCA=='
# org = "Portfolio_Opt"
# url = "http://localhost:8080"
# bucket = "Nifty50"

# client = InfluxDBClient(url=url, token=token, org=org)
# write_api = client.write_api(write_options=SYNCHRONOUS)
nifty50_symbols = {
    "ADANIENT": "Adani Enterprises Ltd.",
    "ADANIPORTS": "Adani Ports and SEZ Ltd.",
    "APOLLOHOSP": "Apollo Hospitals Enterprise Ltd.",
    "ASIANPAINT": "Asian Paints Ltd.",
    "AXISBANK": "Axis Bank Ltd.",
    "BAJAJ-AUTO": "Bajaj Auto Ltd.",
    "BAJFINANCE": "Bajaj Finance Ltd.",
    "BAJAJFINSV": "Bajaj Finserv Ltd.",
    "BHARTIARTL": "Bharti Airtel Ltd.",
    "BPCL": "Bharat Petroleum Corporation Ltd.",
    "BRITANNIA": "Britannia Industries Ltd.",
    "CIPLA": "Cipla Ltd.",
    "COALINDIA": "Coal India Ltd.",
    "DIVISLAB": "Divi's Laboratories Ltd.",
    "DRREDDY": "Dr. Reddy's Laboratories Ltd.",
    "EICHERMOT": "Eicher Motors Ltd.",
    "GRASIM": "Grasim Industries Ltd.",
    "HCLTECH": "HCL Technologies Ltd.",
    "HDFCBANK": "HDFC Bank Ltd.",
    "HDFCLIFE": "HDFC Life Insurance Company Ltd.",
    "HEROMOTOCO": "Hero MotoCorp Ltd.",
    "HINDALCO": "Hindalco Industries Ltd.",
    "HINDUNILVR": "Hindustan Unilever Ltd.",
    "HDFC": "Housing Development Finance Corporation Ltd.",
    "ICICIBANK": "ICICI Bank Ltd.",
    "ITC": "ITC Ltd.",
    "IOC": "Indian Oil Corporation Ltd.",
    "INDUSINDBK": "IndusInd Bank Ltd.",
    "INFY": "Infosys Ltd.",
    "JSWSTEEL": "JSW Steel Ltd.",
    "KOTAKBANK": "Kotak Mahindra Bank Ltd.",
    "LT": "Larsen & Toubro Ltd.",
    "M&M": "Mahindra & Mahindra Ltd.",
    "MARUTI": "Maruti Suzuki India Ltd.",
    "NESTLEIND": "Nestle India Ltd.",
    "NTPC": "NTPC Ltd.",
    "ONGC": "Oil and Natural Gas Corporation Ltd.",
    "POWERGRID": "Power Grid Corporation of India Ltd.",
    "RELIANCE": "Reliance Industries Ltd.",
    "SBILIFE": "SBI Life Insurance Company Ltd.",
    "SHREECEM": "Shree Cement Ltd.",
    "SBIN": "State Bank of India",
    "SUNPHARMA": "Sun Pharmaceutical Industries Ltd.",
    "TCS": "Tata Consultancy Services Ltd.",
    "TATACONSUM": "Tata Consumer Products Ltd.",
    "TATAMOTORS": "Tata Motors Ltd.",
    "TATASTEEL": "Tata Steel Ltd.",
    "TECHM": "Tech Mahindra Ltd.",
    "TITAN": "Titan Company Ltd.",
    "ULTRACEMCO": "UltraTech Cement Ltd.",
}
# val_list = list(nifty50_symbols.values())
# key_list = list(nifty50_symbols.keys())
# count=0
# def safe_float_conversion(value):
#     try:
#         return float(value)
#     except ValueError:
#         return None  # or return a default value, e.g., 0.0 or float('nan')

# # with open('/Users/uddashyakumar/Downloads/nifty500.xls', 'r') as file:
# reader = pd.read_excel('/Users/uddashyakumar/Downloads/nifty500.xls')
# for row in reader:
#     stock_name = row['stock_name']
#     try:
#         position = val_list.index(stock_name)
#         stock_symbol = key_list[position]
#     except:
#         stock_symbol=''
#     # position = val_list.index(stock_name)
#     # stock_symbol = key_list[position] if position != -1 else ''

#     if stock_symbol:
#         for key, value in row.items():
#             if key != 'stock_name':  # Skip the stock name column
#                 float_value = safe_float_conversion(value)
#                 if float_value is not None:  # Ensure that the value is a float
#                     parts = key.rsplit('_', 1)
#                     if len(parts) == 2:
#                         metric, year_suffix = parts
#                         year = {'yr1': '2023', 'yr2': '2022', 'yr3': '2021', 'yr4': '2020', 'yr5': '2019'}.get(year_suffix, None)
#                         if year:
#                             point = Point("stock_metrics")
#                             point.tag("symbol", stock_symbol)
#                             point.field(metric, float_value)
#                             point.time(f"{year}-01-01T00:00:00Z", WritePrecision.NS)
#                             write_api.write(bucket=bucket, org=org, record=point)

# with open('/Users/uddashyakumar/Downloads/nifty500.csv', 'r') as file:
#     reader = csv.DictReader(file)
#     for row in reader:
#         stock_name = row['stock_name']
#         # stock_symbol = nifty50_symbols.get(stock_name)  # Get the stock symbol using the dictionary
#         try:
#             position = val_list.index(stock_name)
#             stock_symbol = key_list[position]
#         except:
#             stock_symbol=''
#         if stock_symbol != None or stock_symbol != '':
#             stock_name = row['stock_name']
#             for key, value in row.items():
#                 count+=1
#                 if key != 'stock_name':  # Skip the stock_name column
#                     print(stock_symbol)
#                     # Splitting the key to extract field name and year
#                     parts = key.rsplit('_', 1)
#                     print(parts)
#                     if len(parts) == 2:
#                         metric, year_suffix = parts
#                         year = {'yr1': '2023', 'yr2': '2022', 'yr3': '2021', 'yr4': '2020', 'yr5': '2019'}.get(year_suffix, None)
#                         if year:
#                             # Create data point
#                             point = Point("stock_metrics")
#                             point.tag("symbol", stock_symbol)
#                             point.field(metric, value)
#                             point.time(f"{year}-01-01T00:00:00Z", WritePrecision.NS)
#                             # print(point)
#                             # Write data to InfluxDB
#                             write_api.write(bucket=bucket, org=org, record=point)
#                             print(f"Data for {stock_name} written to InfluxDB and count is {count}.", end="\r")
# Close the client
# client.close()
import pandas as pd
from influxdb_client import InfluxDBClient, Point, WritePrecision
from influxdb_client.client.write_api import SYNCHRONOUS

# InfluxDB settings
token = 'MlUmh8wWKDAcBiZbBjvJPguGKxoON1ZRqFjVQ_zh8M3NHLcr53WnxbfXX_ByD0Wm7S8G0kb622gj2EX25MzFCA=='
org = "Portfolio_Opt"
url = "http://localhost:8080"
bucket = "Nifty50"

client = InfluxDBClient(url=url, token=token, org=org)
write_api = client.write_api(write_options=SYNCHRONOUS)

nifty50_symbols = {
    "ADANIENT": "Adani Enterprises Ltd.",
    "ADANIPORTS": "Adani Ports and SEZ Ltd.",
    "APOLLOHOSP": "Apollo Hospitals Enterprise Ltd.",
    "ASIANPAINT": "Asian Paints Ltd.",
    "AXISBANK": "Axis Bank Ltd.",
    "BAJAJ-AUTO": "Bajaj Auto Ltd.",
    "BAJFINANCE": "Bajaj Finance Ltd.",
    "BAJAJFINSV": "Bajaj Finserv Ltd.",
    "BHARTIARTL": "Bharti Airtel Ltd.",
    "BPCL": "Bharat Petroleum Corporation Ltd.",
    "BRITANNIA": "Britannia Industries Ltd.",
    "CIPLA": "Cipla Ltd.",
    "COALINDIA": "Coal India Ltd.",
    "DIVISLAB": "Divi's Laboratories Ltd.",
    "DRREDDY": "Dr. Reddy's Laboratories Ltd.",
    "EICHERMOT": "Eicher Motors Ltd.",
    "GRASIM": "Grasim Industries Ltd.",
    "HCLTECH": "HCL Technologies Ltd.",
    "HDFCBANK": "HDFC Bank Ltd.",
    "HDFCLIFE": "HDFC Life Insurance Company Ltd.",
    "HEROMOTOCO": "Hero MotoCorp Ltd.",
    "HINDALCO": "Hindalco Industries Ltd.",
    "HINDUNILVR": "Hindustan Unilever Ltd.",
    "HDFC": "Housing Development Finance Corporation Ltd.",
    "ICICIBANK": "ICICI Bank Ltd.",
    "ITC": "ITC Ltd.",
    "IOC": "Indian Oil Corporation Ltd.",
    "INDUSINDBK": "IndusInd Bank Ltd.",
    "INFY": "Infosys Ltd.",
    "JSWSTEEL": "JSW Steel Ltd.",
    "KOTAKBANK": "Kotak Mahindra Bank Ltd.",
    "LT": "Larsen & Toubro Ltd.",
    "M&M": "Mahindra & Mahindra Ltd.",
    "MARUTI": "Maruti Suzuki India Ltd.",
    "NESTLEIND": "Nestle India Ltd.",
    "NTPC": "NTPC Ltd.",
    "ONGC": "Oil and Natural Gas Corporation Ltd.",
    "POWERGRID": "Power Grid Corporation of India Ltd.",
    "RELIANCE": "Reliance Industries Ltd.",
    "SBILIFE": "SBI Life Insurance Company Ltd.",
    "SHREECEM": "Shree Cement Ltd.",
    "SBIN": "State Bank of India",
    "SUNPHARMA": "Sun Pharmaceutical Industries Ltd.",
    "TCS": "Tata Consultancy Services Ltd.",
    "TATACONSUM": "Tata Consumer Products Ltd.",
    "TATAMOTORS": "Tata Motors Ltd.",
    "TATASTEEL": "Tata Steel Ltd.",
    "TECHM": "Tech Mahindra Ltd.",
    "TITAN": "Titan Company Ltd.",
    "ULTRACEMCO": "UltraTech Cement Ltd.",
}
val_list = list(nifty50_symbols.values())
key_list = list(nifty50_symbols.keys())
# Function to safely convert to float
def safe_float_conversion(value):
    try:
        return float(value)
    except ValueError:
        return None  # or return a default value, e.g., 0.0 or float('nan')

# Load the Excel file
df = pd.read_excel('/Users/uddashyakumar/Desktop/nifty500.xls')  # Make sure the file path is correct

# Iterate over each row in the DataFrame
for index, row in df.iterrows():
    stock_name = row['stock_name']
    try:
        position = val_list.index(stock_name)  # Attempt to find the index of the stock name
        stock_symbol = key_list[position]      # Get the corresponding stock symbol from the key list
    except ValueError:  # Handle the case where the stock name is not found in the list
        stock_symbol = None    
    if stock_symbol:
        for key, value in row.items():
            print(key,'     ',value)
            if key != 'stock_name':  # Skip the 'stock_name' column
                float_value = safe_float_conversion(value)
                if float_value is not None:  # Ensure that the value is a float
                    parts = key.rsplit('_', 1)
                    if len(parts) == 2:
                        metric, year_suffix = parts
                        year = {'yr1': '2023', 'yr2': '2022', 'yr3': '2021', 'yr4': '2020', 'yr5': '2019'}.get(year_suffix, None)
                        if year:
                            # Create a point and write it to InfluxDB
                            point = Point("stock_metrics")
                            point.tag("symbol", stock_symbol)
                            point.field(metric, float_value)
                            point.time(f"{year}-01-01T00:00:00Z", WritePrecision.NS)
                            write_api.write(bucket=bucket, org=org, record=point)
                            print(f"Data for {stock_name} written to InfluxDB.", end="\r")

# Close the client
client.close()
