class Game:

    def __init__(self, name, winner):
        self.name = name
        self.winner = winner

# def who_wins(player1_choice, player2_choice):
#     if player1_choice == player2_choice:
#         return "Its a draw!"
#     elif player1_choice == "rock" and player2_choice == "scissors":
#         return "Player 1 wins playing rock"
#     elif player1_choice == "paper" and player2_choice == "rock":
#         return "Player 1 wins playing paper"
#     elif player1_choice == "scissors" and player2_choice == "paper":
#         return "Player 1 wins playing scissors"
    
#     else:
#         return "Player 2 wins!"
   
def who_wins(player1_choice, player2_choice):
    if player1_choice == "rock" and player2_choice == "scissors":
        return "Player 1 wins playing rock"
    elif player1_choice =="rock" and player2_choice == "paper":
        return "Player 2 wins playing paper"
    elif player1_choice == "paper" and player2_choice == "rock":
        return "Player 1 wins playing paper"
    elif player1_choice == "paper" and player2_choice == "scissors":
        return "Player 2 wins playing scissors"
    elif player1_choice == "scissors" and player2_choice == "paper":
        return "Player 1 wins playing scissors"
    elif player1_choice == "scissors" and player2_choice == "rock":
        return "Player 2 wins playing rock"
    else:
        return "Both players played the same, its a draw!"

    

      
                  
