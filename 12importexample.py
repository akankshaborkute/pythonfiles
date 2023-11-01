import random
roll = random.randint(1,6)
print("The computer rolled a "+str(roll))
guess=int(input("guess the dice roll:\n"))
if guess == roll:
    print("correct! They rolled a "+str(roll) )
else:
    print("Not correct! They rolled a "+str(roll) )    



computer_choice=random.choice(['rock','paper','scissors'])
user_choice=input("input your choice")
if computer_choice==user_choice:
    print("Tie")
if computer_choice=="scissors" and user_choice=="rock":
    print("Win!")

if computer_choice=="rock" and user_choice=="paper":
    print("Win!")

if computer_choice=="paper" and user_choice=="scissors":
    print("Win!")
else:
    print("you loose computer Win")