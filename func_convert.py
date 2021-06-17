import requests
rates = requests.get('https://openexchangerates.org/api/latest.json?app_id=1410ec879b1c4499a82350698777fb15').json()["rates"]

def convert(conv_to: str, num_input: float):
    if v := rates.get(conv_to.upper()):
           return f"{num_input} USD is {float(num_input) * float(v)} {conv_to.upper()}"
    return "Not a valid currency to convert to. The available rates are:\n" + ", ".join(name for name in rates.keys())

