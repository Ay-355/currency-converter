import json
import requests
import sys

def main():
    rates = requests.get('https://openexchangerates.org/api/latest.json?app_id=1410ec879b1c4499a82350698777fb15').json()["rates"]

    convert_to = input('What do you want to convert USD to: ')
    if v := rates.get(convert_to.upper()):
        try:
            val_to = float(input('How much: '))
        except ValueError:
            print("Input has to be a number")
            sys.exit(1)
        print(f"{val_to} USD is {val_to * float(v)} {convert_to.upper()}")
    else:
        print("Not a valid input. The available rates are:\n" +", ".join(name for name in rates.keys()))
        sys.exit(1)

if __name__ == "__main__":
    main()
