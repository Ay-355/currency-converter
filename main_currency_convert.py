#! Imports
import json
import requests


# access API
r = requests.get('https://openexchangerates.org/api/latest.json?app_id=1410ec879b1c4499a82350698777fb15')
ex_rates = r.json()

with open('rates.json', 'w') as f:      #made json file, not needed
    json.dump(ex_rates, f, indent=4)

    
#! Code
rates = ex_rates['rates']                   #acess rate part

convertTo = input('What do you want to convert USD to: ')    #first question


for name, value in rates.items():
    if convertTo in name:                          #checks if input in json file
        valTo = float(input('How much: '))          #asks how much you want to convert
        valFloat = float(value)
        result = valTo*valFloat                    #math
        print(f"{valTo} USD is {result} {convertTo}") 
        break   
else:
    print('That is not a valid input!')   #error if don't put correct one in
    print(f"The available rates are:")
    for name in rates.keys():               #gives available things to convert to
        print(f"{name}")







