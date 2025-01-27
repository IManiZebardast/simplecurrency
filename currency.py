import requests

def get_exchange_rates():
    url = "https://api.freecurrencyapi.com/v1/latest?apikey=fca_live_xkuF4kFbJ1QyY0Cne1avzw4LzvgUIXBjqBhHYavZ"
    response = requests.get(url)
    return response.json()['data']

def main():
    data = get_exchange_rates()

    currencies = {'AUD': 1.5890902106, 'BGN': 1.865300307, 'BRL': 5.9100506841, 'CAD': 1.4384701495, 
                  'CHF': 0.9068501237, 'CNY': 7.2575810116, 'CZK': 23.970334466, 'DKK': 7.1282813691, 
                  'EUR': 0.9552900958, 'GBP': 0.8027701124, 'HKD': 7.7857614713, 'HRK': 6.7958212077, 
                  'HUF': 389.0976577479, 'IDR': 16187.014441405, 'ILS': 3.5771705962, 'INR': 86.3096129146,
                  'ISK': 139.6920877923, 'JPY': 155.7899880261, 'KRW': 1429.5051249323, 'MXN': 20.4247428258, 
                  'MYR': 4.3848406556, 'NOK': 11.2197314086, 'NZD': 1.7567903034, 'PHP': 58.2850596472, 
                  'PLN': 4.0218607244, 'RON': 4.7532609059, 'RUB': 97.8429698838, 'SEK': 10.9554511368, 
                  'SGD': 1.3473901531, 'THB': 33.6574958031, 'TRY': 35.6292546441, 'USD': 1, 'ZAR': 18.4822936912}

    currencies_list = list(currencies.keys())

    currency = input(f'Choose your currency from the list {currencies_list}: ').upper()

    if currency in data:
        main_price = data[currency]
        print(f'One {currency} is equal to {main_price} USD.')
    else:
        print('Invalid currency. Please choose from the list.')

if __name__ == "__main__":
    main()
