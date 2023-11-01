temprature=50
if temprature>80:
    print("its too hot.")
    print("stay inside!")
elif temprature<60:
    print("its too cold.")
    print("stay inside!")
else:
    print("enjoy Outdoors")    


temprature=76
if temprature>80 or temprature<60:

    print("stay inside!")
else:
    print("enjoy Outdoors")    


temprature=76
forcast='rainy'
if temprature<80 and forcast=="rainy":

    print("Go OutSide!")
else:
    print("stay inside!")


temprature=76
forcast='rainy'
if temprature<80 and forcast!="rainy":

    print("Go OutSide!")
else:
    print("stay inside!")    


computer_choice='scissors'
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