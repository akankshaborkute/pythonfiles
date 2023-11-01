i=0
j=0
while i<3:
    while j<3:
        # print("praya")
        j+=1
    # print("praya")
    i+=1

while True:
    n=int(input("what is n"))
    if n>0:
        break

for _ in range(n):
    print("meow")


def main():
    meow(3)

def meow(n):
    for _ in range(n):
        print("praaya")
main()




def main():
    number=get_number()
    meow(number)



def get_number():
    while True:
        n=int(input("what is n"))
        if n>0:
            return n
def meow(n):
    for _ in range(n):
        print("prafull_raaya")
main()