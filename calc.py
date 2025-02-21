import requests

API_URL = "https://api.exchangerate-api.com/v4/latest/"

def convert_currency(amount, from_currency, to_currency):
    url = API_URL + from_currency
    response = requests.get(url)
    
    if response.status_code != 200:
        return "Error: Unable to fetch exchange rates. Check currency codes or API availability."
    
    data = response.json()
    
    if "rates" not in data:
        return "Error: Invalid response from API."
    
    rates = data["rates"]
    
    if to_currency not in rates:
        return f"Error: Unsupported currency '{to_currency}'."
    
    converted_amount = amount * rates[to_currency]
    return f"{amount} {from_currency} = {converted_amount:.2f} {to_currency}"

# Example usage
amount = float(input("Enter amount: "))
from_currency = input("From currency (e.g., USD): ").upper()
to_currency = input("To currency (e.g., EUR): ").upper()

result = convert_currency(amount, from_currency, to_currency)
print(result)
