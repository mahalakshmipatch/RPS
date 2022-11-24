from random import choice

def showboard(p,c):
    print("***********************")
    print("Score Board (Graph)")
    print("***********************")
    print("  |")
    print(f"P | {p*'x'}")
    print("  |")
    print(f"C | {c*'x'}")
    print("  |")
    print("-------------")
    print("  |  Score ->")
    print("***********************")
    print("")

rps = ("rock","paper","scissors")
rounds = input("How many rounds do you want to play? ")
if(rounds.isnumeric()):
    rounds=int(rounds)
else:
    print("Invalid Input")
    quit()
print("")
cScore = 0
pScore = 0
pWinner = "Player"
cWinner = "Computer"
tWinner = "Tie"
tieBreaker=True


while(tieBreaker== True):
    for i in range(0,rounds):
        computer = choice(rps)
        print("-----------------------")
        print("")
        player = input("Enter Rock, Paper, or Scissors: ")
        print("")
        player = player.lower()
        print(f"Player: {player}")
        print(f"Computer: {computer}")
        winner = tWinner

        if(computer==player):
            winner=tWinner

        elif(player=="rock"):
            if(computer=="paper"):
                winner = cWinner
                cScore+= 1
            else:
                winner = pWinner
                pScore+= 1

        elif(player=="paper"):
            if(computer=="scissors"):
                winner = cWinner
                cScore+= 1
            else:
                winner = pWinner
                pScore+= 1

        elif(player=="scissors"):
            if(computer=="rock"):
                winner = cWinner
                cScore+= 1
            else:
                winner = pWinner
                pScore+= 1

        else:
            print("Invalid input")
        print("")

        if(winner==tWinner):
            print("This round is a tie.")
        else:
            print(f"The round winner is {winner}")
        print("")

    print("-----------------------")
    print(f"The score of the player : {pScore}")
    print(f"The score of the computer : {cScore}")
    print("-----------------------")
    print("")
    showboard(pScore,cScore)


    if(pScore==cScore):
        print("No winner, it's a tie.")
        print("We need a tie breaker round.")
        tieBreaker=True
        rounds=1
    elif(pScore>cScore):
        tieBreaker=False
        print("The final winner is Player.")
    else:
        print("The final winner is computer.")
        tieBreaker=False
    print("")
 