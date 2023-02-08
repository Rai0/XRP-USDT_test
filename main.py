from requests import get
from pandas import DataFrame
from datetime import datetime

main_binance_endpoint = "https://api.binance.com/api/v3/"

requests_price = "ticker/price"
requests_klines = "klines"
requests_interval = "1h"
xrpusd = "XRPUSDT"

def looper():
    last_best_price_update = None
    while True:
        if not last_best_price_update or last_best_price_update.hour != datetime.now().hour:
            best_h_price = get(f"{main_binance_endpoint}{requests_klines}?symbol={xrpusd}&interval={requests_interval}&limit=1000").json()
            try:    
                df = DataFrame(best_h_price).iloc[:, :5]
                df.columns = list("tohlc")
                max_price = float(df["h"].max())
                one_p = max_price / 100
                last_best_price_update = datetime.now()
            except:
                """тут должна быть нормальная обработка конкретной ошибки"""
                pass
        
        price = get(f"{main_binance_endpoint}{requests_price}?symbol={xrpusd}").json()
        try:
            act_price = float(price["price"])
        except:
            """тут должна быть нормальная обработка конкретной ошибки"""
            pass

        if max_price and act_price and max_price - act_price >= one_p:
            print(f"max: {max_price}, act_price: {act_price}, 1%: {one_p}")
            print (f'[INFO] актуальная цена ниже максимальной на {"{:.2f}".format((max_price - act_price) / one_p)}%')

if __name__ == "__main__":
    looper()
    