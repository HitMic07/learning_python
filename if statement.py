hot = False
cold = False

if hot:
    print('Today is hot')
    print('Drink water')

elif cold:
    print('Today is cold')
    print('Stay inside')

else:
    print("Its a lovely day")

# WHEN BOTH STATEMENT IS FALSE

price = 100000
good_credit = False

if good_credit:
    down_payment = 0.1 * price

else:
    down_payment = 0.2 * price

print(f" down payment: ${down_payment}")


