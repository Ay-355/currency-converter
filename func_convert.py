import requests

r = requests.get('https://openexchangerates.org/api/latest.json?app_id=1410ec879b1c4499a82350698777fb15')
ex_rates = r.json()


rates = ex_rates['rates']             #access rates part of json file

def convert(convTo, numInput):                  #define function, currency to convert to and how much we want to convert
    for name, value in rates.items():           #assigns variables to key, value in file
        if convTo in name:                      #if input is in the list of available things to convert to
            numInputFloat = float(numInput)          
            result = value*numInputFloat        #math
            print(f"{numInputFloat} USD is {result} {convTo}")
            break

convert('INR', 45)    #function test
