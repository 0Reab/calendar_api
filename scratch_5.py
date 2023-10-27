mistakes = []

running = True

while running:
    print("1 - time"
          "2 - my tactic"
          "3 - opponent tactic"
          "4 - endgame"
          "5 - opening"
          "6 - queen hang"
          "7 - free piece"
          "8 - bad calculation"
          "9 - failed attack")
    if input("1"):
        mistakes.append("time")
    if input("2"):
        mistakes.append("my tactic")
    if input("3"):
        mistakes.append("opponent tactic")
    if input("4"):
        mistakes.append("endgame")
    if input("5"):
        mistakes.append("opening")
    if input("6"):
        mistakes.append("queen hang")
    if input("7"):
        mistakes.append("free piece")
    if input("8"):
        mistakes.append("bad calculation")
    if input("9"):
        mistakes.append("failed attack")
