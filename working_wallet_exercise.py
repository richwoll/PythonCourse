#wallet
wallet = {'GBP': 50.00,'HUF':40000.00,'USD': 80.00,'EUR':25.00}
Pounds = wallet.get('GBP')
print("Amount of GBP:", Pounds)

def working_wallet(wallet_dict:Dict, currency:str, amount_spent:float) :
    for wallet_currency,amount in wallet_dict.items() :
        if currency == wallet_currency :
            if amount_spent <= amount :
                wallet_dict[wallet_currency] -= amount_spent
                return amount_spent
            else :
                wallet_dict[wallet_currency]=0
                return amount

print(working_wallet(wallet, 'GBP', 33))

print("Amount of GBP:", wallet['GBP'])

class EmptyWalletError(Exception):
    pass

def working_wallet2(wallet_dict:Dict, currency:str, amount_spent:float) :
    remaining_amount = wallet_dict.get(currency,0)
    if wallet_dict[currency] >= amount_spent:
        wallet_dict[currency] = remaining_amount - amount_spent
        return min([remaining_amount,amount_spent])
    else:
        raise EmptyWalletError('Not enough money in wallet')

try:
    working_wallet2(wallet,'HUF',1000)
except EmptyWalletError:
    print('you outta money fool')

print(working_wallet2(wallet,'HUF',1000.00))
