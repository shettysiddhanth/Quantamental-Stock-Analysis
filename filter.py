from influxdb_client import InfluxDBClient

# Define your InfluxDB credentials and connection details
token = 'MlUmh8wWKDAcBiZbBjvJPguGKxoON1ZRqFjVQ_zh8M3NHLcr53WnxbfXX_ByD0Wm7S8G0kb622gj2EX25MzFCA=='
org = "Portfolio_Opt"
url = "http://localhost:8080"
bucket = "Nifty50"

# Connect to the InfluxDB instance
client = InfluxDBClient(url=url, token=token, org=org)

# Define the benchmarks for each financial ratio
benchmarks = {
    'Basic EPS (Rs.)': 25,
    'Return on Networth / Equity (%)': 15,
    # 'Total Debt/Equity (X)': 1,
    # 'Asset Turnover Ratio (%)': 0.88,
    'Current Ratio (X)': 1.5,
    # 'Quick Ratio (X)': 1,
    # 'Cash EPS (Rs.)': 5,
    # 'Dividend Payout Ratio (CP) (%)': 30,
    # 'EV/EBITDA (X)': 10,
    # 'Net Profit Margin (%)': 10,
    'PBIT Margin (%)': 12,
    # 'PBT Margin (%)': 10,
    # 'Price/BV (X)': 3,
    # 'Return on Assets (%)': 5,
    'Return on Capital Employed (%)': 10
}
nifty50_symbols = [
    "ADANIPORTS", "ASIANPAINT", "AXISBANK", "BAJAJ-AUTO", "BAJFINANCE",
    "BAJAJFINSV", "BPCL", "BHARTIARTL", "BRITANNIA", "CIPLA",
    "COALINDIA", "DIVISLAB", "DRREDDY", "EICHERMOT", "GRASIM",
    "HCLTECH", "HDFCBANK", "HDFCLIFE", "HEROMOTOCO", "HINDALCO",
    "HINDUNILVR", "HDFC", "ICICIBANK", "ITC", "IOC",
    "INDUSINDBK", "INFY", "JSWSTEEL", "KOTAKBANK", "LT",
    "M&M", "MARUTI", "NTPC", "NESTLEIND", "ONGC",
    "POWERGRID", "RELIANCE", "SBILIFE", "SHREECEM", "SBIN",
    "SUNPHARMA", "TCS", "TATACONSUM", "TATAMOTORS", "TATASTEEL",
    "TECHM", "TITAN", "UPL", "ULTRACEMCO", "WIPRO"
]

# Function to query data and compare against benchmarks
def fetch_and_evaluate():
    qualifying_companies = {}
    query_api = client.query_api()

    for symbol in nifty50_symbols:
        all_meet_benchmark = True
        for ratio, benchmark in benchmarks.items():
            query = f'''
                from(bucket: "Nifty50")
                |> range(start: -2y)
                |> filter(fn: (r) => r["_measurement"] == "stock_metrics")
                |> filter(fn: (r) => r["_field"] == "{ratio}")
                |> filter(fn: (r) => r["symbol"] == "{symbol}")
            '''
            result = query_api.query(org=org, query=query)
            meets_benchmark = False
            for table in result:
                for record in table.records:
                    if record.get_value() >= benchmark:
                        meets_benchmark = True
                        break
                if meets_benchmark:
                    break
            if not meets_benchmark:
                all_meet_benchmark = False
                break
        if all_meet_benchmark:
            qualifying_companies[symbol] = True

    return [company for company, valid in qualifying_companies.items() if valid]

# Run the function and print qualifying companies
qualifying_companies = fetch_and_evaluate()
print("Companies that meet or exceed all benchmarks:", qualifying_companies)

# Close the client
client.close()
