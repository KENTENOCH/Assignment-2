#Script for car prices
#prices of cars are in US dollars

car_prices = {
    'hammer': 5500,
    'ferrari': 5600,
    'ford': 28000,
    'bughatti': 95300,
    'Mecury': 1300,
    'jaguar': 48000,
    'honda': 115000,
    'chevrolet': 411500,
    'Weismann': 100000,
    'tesla': 63000,
    'mercedes benz': 910000,
    'porsche': 4300,
    'acura': 42000,
    'pontiac': 42500,
    'lincoln': 61300,
    'alfa romeo': 16070,
    'saab': 35000,
    'saturn': 21000,
    'zanella': 29000,
    'seat': 83500,
    'Nissan': 13000,
    'maserati': 56000,
    'smart': 29000,
    'renault': 321000,
    'subaru': 15300,
    'peugeot': 31420,
    'Daihatsu': 381000,
    'Aspark': 76000,
    'Darcia': 321000,
    'dodge': 21000
}

car_brand = input('Enter car brand: ').lower()

if car_brand in car_prices:
    print(f"The price of {car_brand} is ${car_prices[car_brand]:,}")
else:
    print(f"Sorry, {car_brand} is not in our list.")
https://github.com/users/KENTENOCH/emails/242076628/confirm_verification/33174332?via_launch_code_email=true
    