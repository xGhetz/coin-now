import requests
from tkinter import *
from tkinter import ttk

api_key = "YOUR_API_KEY"
url = "https://pro-api.coinmarketcap.com/v1/cryptocurrency/quotes/latest"

def get_coin_price(coin, currency):
    try:
        r = requests.get(url, headers={'Accepts': 'application/json', 'X-CMC_PRO_API_KEY': api_key}, params={'symbol': coin, 'convert': currency})
        r.raise_for_status()
        get_price = r.json()
        data = get_price['data'][coin]['quote'][currency]['price']
        return f"${data:.2f}"
    except requests.exceptions.RequestException as e:
        print(f"Request error: {e}")
        return "Error fetching price"
    except Exception as e:
        print(f"Error: {e}")
        return "Error fetching price"

def update_price_label():
    coin = coin_input.get()
    currency = coin_to_convert.get()
    price = get_coin_price(coin, currency)
    coin_input_var.set(f"{coin}")
    coin_to_convert_var.set(f"{currency}")
    price_label.config(text=price)

root = Tk()
root.title("Coin Now")

coin_input_var = StringVar()
coin_to_convert_var = StringVar()

frame = ttk.Frame(root, padding="3 3 10 10")
frame.grid()

Label(frame, text="Coin:").grid(row=0, column=0, padx=10, pady=10)
coin_input = Entry(frame, textvariable=coin_input_var, width=20)
coin_input.grid(row=0, column=1, padx=10, pady=10)
coin_input.insert(0, 'BTC')

Label(frame, text="Convert to:").grid(row=1, column=0, padx=10, pady=10)
coin_to_convert = Entry(frame, textvariable=coin_to_convert_var, width=20)
coin_to_convert.grid(row=1, column=1, padx=10, pady=10)
coin_to_convert.insert(0, 'USD')

search_button = Button(frame, text="Search", command=update_price_label, width=10)
search_button.grid(row=2, columnspan=2, padx=15, pady=15)

price_label = Label(frame, text="", font=("Arial", 14, "bold"))
price_label.grid(row=3, columnspan=2)

root.mainloop()