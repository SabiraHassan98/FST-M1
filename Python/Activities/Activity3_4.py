#Player1: Rock, Paper, or Scissors
#Player2: Rock, Paper, or Scissors

#Rules:
#Rock beats Scissors
#Scissors beats Paper
#Paper beats Rock
while (True):

    player1 = input( "Enter Player1 choise- rock,paper,scissor: ").lower()
    player2 = input ("Enter Player2 choice:- rock,paper,scissor ").lower()
    # need to add a condition to enter a right choice
    #if player1 != ["rock","paper","Scissor"].lower()
    print()

    if player1 == player2:
        print("Tie!")
    elif player1 == "rock":
        if player2 == "scissor":
            print("Player 1 is the winner")
        else:
            print ("Player2 is a winner")   
    elif player1 == "scissor":
        if player2 == "paper":
            print("Player2 is the winner")
        else:
            print ("Player1 is a winner") 
    elif player1 == "paper":
        if player2 == "rock":
            print("Player 1 is the winner")
        else:
            print ("Player2 is a winner")  

    play_again = input ("Do you want to play again: ").lower()
    if play_again == "y" or play_again == "yes":
        pass
    else :
        break

print("Thank you for playing! ")


