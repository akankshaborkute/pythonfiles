students={
    "shivaji":"prafull",
    "hindu":"akanksha",
    "giis":"raaya"
}
# print(students["shivaji"])
# print(students["hindu"])
# print(students["giis"])
i=0
for student in students:
    i += 1
    print(i,")",student,students[student], sep=", ")



students=[
    {"shivaji":"prafull","hindu":"akanksha","giis":"raaya"},
    {"shivaji":"pratiksha","hindu":"priya","giis":"riku"},
    {"shivaji":"madhuri","hindu":"shalini","giis":"mysha"},
    {"shivaji":"sunil","hindu":"chiku","giis":None}

]
i=0
for student in students:
    i += 1
    print(i,student["shivaji"],student["hindu"],student["giis"], sep=", ")

def main():
    print_column(5)
    print_row(4)
    print_squre(3)
def print_column(height):
    for _ in range(height):
        print("#\n"*height,end="")
def print_row(width):
    print("?"*width)

def print_squre(size):
    for i in range(size):
        for j in range(size):
            print("#", end="")
            # print("#"*size)
        print()



main()