# Get details of a loan
money_owed = float(input("How much money do you owe?\n")) # $50,000
apr = float(input("What is the annual percentage rate (APR) on the loan?\n")) # 3.92
payment = float(input("What is your monthly payment?\n")) # $1,000
months = int(input("How many months do you want to simulate?\n")) # 24

monthly_rate = apr / 100 / 12

for i in range(months):
    print("Month", i + 1)

    # Calculate interest to pay
    interest_paid = money_owed * monthly_rate

    # Add in interest
    money_owed += interest_paid

    if (money_owed - payment) < 0:
        print('The last payment is', money_owed)
        print('You paid off the loan in', i + 1, 'months!')
        break

    # Make payment
    money_owed -= payment

    print('Paid', payment, 'of which', interest_paid, 'was interest', end = ' ')
    print('You now owe', money_owed)