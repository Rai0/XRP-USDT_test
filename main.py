from requests import get
from pandas import DataFrame

main_binance_endpoint = "https://api.binance.com/api/v3/"

requests_price = "ticker/price"
requests_klines = "klines"
requests_interval = "1h"

xrpusd = "XRPUSDT"

price = get(f"{main_binance_endpoint}{requests_price}?symbol={xrpusd}").json()

best_h_price = get(f"{main_binance_endpoint}{requests_klines}?symbol={xrpusd}&interval={requests_interval}").json()

# print(best_h_price)

df = DataFrame(best_h_price).iloc[:, :5]

df.columns = list("tohlc")

# print(price["price"])
print(df["h"].max())