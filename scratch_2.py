deposit = input("Deposit amount: ")
bet = 0
valid_bet = False
valid_deposit = False

while valid_deposit == False:
    try:
        balance = int(deposit)
        valid_deposit = True
    except:
        valid_deposit = False
        print("Invalid deposit.")
        deposit = input("Try depositing again: ")

if balance <= 0:
    print("Balance is 0")


bet_amount = input("Bet amount: ")

while valid_bet == False:
    try:
        bet = int(bet_amount)
        valid_bet = True
        print("Bet is valid.")
    except:
        print("Invalid bet.")
        bet = input("Try betting again: ")

if bet < balance:
    valid_bet = False
    print("Insuficient funds.")


if bet <= 0:
    valid_bet = False
    print("Invalid bet.")

else:
    valid_bet = True

if valid_bet == True:
    print("Bet placed.")



print(balance)
print(bet)
print(valid_bet)