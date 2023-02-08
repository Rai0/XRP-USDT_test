from requests import get

main_binance_endpoint = "https://api.binance.com/api/v3/"

requests_price = "ticker/price"
requests_klines = "klines"
requests_interval = "1s"

xrpusd = "XRPUSDT"

price = get(f"{main_binance_endpoint}{requests_price}?symbol={xrpusd}").json()
best_h_price = get(f"{main_binance_endpoint}{requests_klines}?symbol={xrpusd}&interval={requests_interval}").text

# print(price["price"])
print(best_h_price)