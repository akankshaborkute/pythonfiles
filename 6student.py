# def main():
#     name=get_name()
#     house=get_house()
#     print(f"{name} from {house}")

# def get_name():
#     na=input("Name: ")
#     return na

# def get_house():
#     ho=input("House: ")
#     return ho

# if __name__=="__main__":
#     main()


# def main():
#     name, house=get_student()
#     print(f"{name} from {house}")

# def get_student():
#     na=input("Name: ")
#     ho=input("House: ")
#     return na, ho

# if __name__=="__main__":
#     main()

#################Touples

# def main():
#     student=get_student()
#     print(f"{student[0]} from {student[1]}")

# def get_student():
#     na=input("Name: ")
#     ho=input("House: ")
#     return (na, ho)

# if __name__=="__main__":
#     main()


################

# def main():
#     student=get_student()
#     if student[0]=="Rafulls":
#         student[1]="Raaya"
#     print(f"{student[0]} from {student[1]}")

# def get_student():
#     na=input("Name: ")
#     ho=input("House: ")
#     return (na, ho)

# if __name__=="__main__":
#     main()


######### Dictionaries


# def main():
#     student=get_student()
#     if student[0]=="Rafulls":
#         student[1]="Raaya"
#     print(f"{student[0]} from {student[1]}")

# def get_student():
#     na=input("Name: ")
#     ho=input("House: ")
#     return [na, ho]

# if __name__=="__main__":
#     main()



# def main():
#     student=get_student()
#     print(f"{student['na']} from {student['ho']}")

# def get_student():
#     stud={}
#     stud["na"]=input("Name: ")
#     stud['ho']=input("House: ")
#     return stud

# if __name__=="__main__":
#     main()



def main():
    student=get_student()
    if student["name"]=="prafull":
        student["house"]="borkute"
    print(f"{student['name']} from {student['house']}")

def get_student():
    na=input("Name: ")
    ho=input("House: ")
    return {"name":na,"house":ho}

if __name__=="__main__":
    main()



