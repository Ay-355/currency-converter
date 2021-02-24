import json
import requests

r = requests.get('https://openexchangerates.org/api/latest.json?app_id=1410ec879b1c4499a82350698777fb15')
ex_rates = r.json()

with open('rates.json', 'w') as f:
    json.dump(ex_rates, f, indent=4)

rates = ex_rates['rates']

convertTo = input('What do you want to convert USD to: ')


for name, value in rates.items():
    if convertTo in name:
        valTo = float(input('How much: '))
        valFloat = float(value)
        result = valTo*valFloat
        print(f"{valTo} USD is {result} {convertTo}")
        break
else:
    print('That is not a valid input!')
    print(f"The available rates are:")
    for name in rates.keys():
        print(f"{name}")







