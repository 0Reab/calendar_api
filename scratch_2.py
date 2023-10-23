import random

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
    except:
        valid_bet = False
        print("Invalid bet.")
        bet = input("Try betting again: ")

if bet > balance:
    valid_bet = False
    print("Insuficient funds.")



if bet <= 0:
    valid_bet = False
    print("Can bet 0 or lower.")

row_1 = [random.randrange(1,4) for i in range(1,4)]
row_2 = [random.randrange(1,4) for i in range(1,4)]
row_3 = [random.randrange(1,4) for i in range(1,4)]

for i in row_1:
    result_1 = 0
    result_1 += i * len(row_1)
for i in row_2:
    result_2 = 0
    result_2 += i * len(row_2)
for i in row_3:
    result_3 = 0
    result_3 += i * len(row_3)


print(balance)
print(bet)
print(valid_bet)