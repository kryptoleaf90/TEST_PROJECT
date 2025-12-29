import random

response = ("rock","paper","scissors")



is_running = True
print("-----CLASSIC RPS-----")
while is_running:
   player=None
   while player not in response:
    player = input("enter response:")
    computer = random.choice(response)
    if player == computer:
        print("TIE!")
    elif player == "rock" and computer == "scissors":
        print("YOU WIN!!")
    elif player == "scissors" and computer == "paper":
        print("YOU WIN!!")
    elif player == "paper" and computer == "rock":
        print("YOU WIN!!")
    else:
        print("YOU LOOSE!!")
    again=input("play again?(y/n):")
    if again!="y":
        is_running=False