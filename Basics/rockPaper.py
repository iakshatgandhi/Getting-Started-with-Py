import random

def get_choices():
    player_choice = input("enter your choice(rock, paper or scissors): ")
    options = ["rock", "paper", "scissors"]
    computer_choice = random.choice(options)
    choices = {"player":player_choice,"computer":computer_choice}
    return choices

def check_win(player, computer):
    # string concatenation
    #print("you chose "+ player + " and the computer chose "+ computer)
    #one more way is to use the f strings
    print(f"you choose {player} and the computer choose {computer}")
    if(player==computer):
        return "it's a tie"
    elif(player=="rock"):
        if(computer=="scissors"):
            return "rock smashes the scissors, You won!!! "
        else:
            return "paper covers the rock, you lose"
    elif(player=="paper"):
        if(computer=="scissors"):
            return "scissor cuts the paper, you lose "
        else:
            return "paper covers the rock, you won!!!"
    elif(player=="scissors"):
        if(computer=="paper"):
            return "scissor cuts the paper, you won!!!"
        else:
            return "rock smashes the scissors, You lose"
    else:
        return "choose correctly 😊"


choices = get_choices()
p_choice = choices["player"]
c_choice = choices["computer"]

result = check_win(p_choice,c_choice)
print(result)