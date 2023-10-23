balance = 0
bet = 0
valid_bet = None

def deposit(amount):
    try:
        balance = int(amount)
    except:
        print("Invalid deposit.")
    if balance <= 0:
        print("Balance is 0")


def bet(bet_amount):
    if bet_amount < balance:
        valid_bet = False
        print("Insuficient funds.")

    if bet_amount <= 0:
        valid_bet = False
        print("Invalid bet.")

    else:
        bet = bet_amount
        valid_bet = True
        print("Bet placed.")


deposit(input("Deposit amount: "))
bet(input("Bet amount: "))

print(balance)
print(bet)
print(valid_bet)