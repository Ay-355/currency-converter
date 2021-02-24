import requests

r = requests.get('https://openexchangerates.org/api/latest.json?app_id=1410ec879b1c4499a82350698777fb15')
ex_rates = r.json()


rates = ex_rates['rates']

def convert(convTo, numInput):
    for name, value in rates.items():
        if convTo in name:
            numInputFloat = float(numInput)
            result = value*numInputFloat
            print(f"{numInputFloat} USD is {result} {convTo}")
            break

convert('INR', 45)
