import yfinance as yf

def get_nvidia_price():
    nvda = yf.Ticker("NVDA")
    current_price = nvda.fast_info.last_price
    if current_price is not None:
        return current_price
    else:
        raise Exception("Error fetching NVIDIA price")