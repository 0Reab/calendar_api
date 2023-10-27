mistakes = []
file = open('chess.txt','w')
running = True

while running:
    print("1 - time\n"
          "2 - my tactic\n"
          "3 - opponent tactic\n"
          "4 - endgame\n"
          "5 - opening\n"
          "6 - queen hang\n"
          "7 - free piece\n"
          "8 - bad calculation\n"
          "9 - failed attack\n"
          "q - SAVE & QUIT\n")
    if input()== "1":
        mistakes.append("time")
    if input()== "2":
        mistakes.append("my tactic")
    if input()== "3":
        mistakes.append("opponent tactic")
    if input()== "4":
        mistakes.append("endgame")
    if input()== "5":
        mistakes.append("opening")
    if input()== "6":
        mistakes.append("queen hang")
    if input()== "7":
        mistakes.append("free piece")
    if input()== "8":
        mistakes.append("bad calculation")
    if input()== "9":
        mistakes.append("failed attack")
    if input()== "q":
        for i in mistakes:
            file.write(i + "\n")
        file.close()
        running = False