prices = {
    "Masala Chai":80,
    "Green Tea": 40,
    "Spicy Tea":60
}

new_prices = {tea:price+10 for tea, price in prices.items()}
print(new_prices)