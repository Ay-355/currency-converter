import json
import requests

js = requests.get('https://openexchangerates.org/api/latest.json?app_id=1410ec879b1c4499a82350698777fb15').json()

rates = js['rates']

convert_to = input('What do you want to convert USD to: ')

for name, value in rates.items():
    if convert_to.upper() == name:
        try:
            val_to = float(input('How much: '))
        except ValueError:
            print("Input has to be a number")
            break
        print(f"{val_to} USD is {val_to * float(value)} {convert_to.upper()}")
        break   
else:
    print("Not a valid input. The available rates are:\n" + ", ".join(name for name in rates.keys()))
