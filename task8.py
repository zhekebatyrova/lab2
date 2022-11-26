def addToBankAccount(money, a):
    return money + a

def substractFromBankAccount(money, a):
    return money - a

def moneyConversion(money, ex_from, ex_to):
    match ex_from, ex_to:
        case 'USD', 'KZT':
            return money * 470
        case 'KZT', 'USD':
            return money / 470
        case _:
            return 'Invalid parameters'

print(addToBankAccount(200,300))
print(substractFromBankAccount(600,300))
print(moneyConversion(400,'KZT', 'USD'))
