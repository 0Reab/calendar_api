import matplotlib.pyplot as plt
import numpy as np

mistakes = []
file = open('chess.txt','w')
running = True
instructions = ("1 - time\n"
          "2 - my tactic\n"
          "3 - opponent tactic\n"
          "4 - endgame\n"
          "5 - opening\n"
          "6 - queen hang\n"
          "7 - free piece\n"
          "8 - bad calculation\n"
          "9 - failed attack\n"
          "q - SAVE & QUIT\n"
          "s - SHOW PLOT\n")

print(instructions)
while running == True:
    choice = input()
    if choice== "1":
        mistakes.append("time")
    elif choice== "2":
        mistakes.append("my tactic")
    elif choice== "3":
        mistakes.append("opponent tactic")
    elif choice== "4":
        mistakes.append("endgame")
    elif choice== "5":
        mistakes.append("opening")
    elif choice== "6":
        mistakes.append("queen hang")
    elif choice== "7":
        mistakes.append("free piece")
    elif choice== "8":
        mistakes.append("bad calculation")
    elif choice== "9":
        mistakes.append("failed attack")
    elif choice== "s":
        y = np.array(mistakes)
        plt.hist(y)
        plt.show()
    elif choice== "q":
        for i in mistakes:
            file.write(i + "\n")
        file.close()
        running = False