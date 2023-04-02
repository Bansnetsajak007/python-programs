import random
from unittest import result

def generate(rand_num):
    if rand_num==1:
        computer_='R'
    
    elif rand_num==2:
        computer_='P'

    elif rand_num==3:
        computer_="S"

    return computer_



def gameWin(comp_choice,user_choice):
    if user_choice== comp_choice:
        return "Game is Tie"

    if (user_choice=='R' and comp_choice=='P'):
        return "you lose the game"

    if (user_choice=='R' and comp_choice=='S'):
        return "you win the game👍🙌"

    if (user_choice=='P' and comp_choice=='R'):
        return "you win the game👍🙌"

    if (user_choice=='P' and comp_choice=='S'):
        return "you lose the game"

    if (user_choice=='S' and comp_choice=='R'):
        return "you lose the game"

    if (user_choice=='S' and comp_choice=='P'):
        return "you win the game👍🙌"




    

win,lose,tie=0,0,0
while True:
    rand_num=random.randint(1,3)

    user_choice= input("Rock(R),Paper(P),Scissors(S):")

    comp_choice=generate(rand_num)


    ressult=gameWin(comp_choice,user_choice)

    if ressult=="Game is Tie":
        tie+=1

    if ressult=="you win the game👍🙌":
        win+=1

    if ressult== "you lose the game":
        lose+=1

    print(ressult)
    print(f"you {user_choice} and computer choses {comp_choice} so the result is {ressult}")
    print(f"Win: {win}")
    print(f"Lose: {lose}")
    print(f"Tie: {tie}")




