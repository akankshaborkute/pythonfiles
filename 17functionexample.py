import random
def greeting(name):
    print('Hello',name)

arg=input("Enter your name:")
arg1=input("Enter your name:")
greeting(arg)

def greeting1():
    print('Hello',arg)

greeting1()

def greeting2(name):
    print('Hello',name)

greeting2(arg1)

def addition(ar1,ar2):
    return ar1+ar2

def rolldice():
    dicetottal=random.randint(1,6) + random.randint(1,6)
    return dicetottal


def main():
    a=float(input("Enter value one "))
    b=float(input("Enter value two "))
    prc=addition(a,b)
    print(prc)
    player1=input("Enter player one name:")
    player2=input("Enter player two name:")
    roll1=rolldice()
    roll2=rolldice()
    print(player1, "The Player one rolled dice",roll1)
    print(player2, "The Player two rolled dice",roll2)
    if roll1>roll2:
        print(player1,'Wins!')
    elif roll1<roll2:
        print(player2,'Wins!')
    else:
        print("Tie")
          
main()
