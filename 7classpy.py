# class Student:
#     ...


# def main():
#     student=get_student()
#     print(f"{student.na} from {student.ho}")

# def get_student():
#     student=Student()
#     student.na=input("Name: ")
#     student.ho=input("House: ")
#     return student

# if __name__=="__main__":
#     main()


# class Student:
#     def __init__(self, name, house):
#         self.na=name
#         self.ho=house
# def main():
#     student=get_student()
#     print(f"{student.na} from {student.ho}")

# def get_student():
    
#     na=input("Name: ")
#     ho=input("House: ")

#     student=Student(na,ho)
#     return student

# if __name__=="__main__":
#     main()




# class Student:
#     def __init__(self, name, house):
#         self.na=name
#         self.ho=house
# def main():
#     student=get_student()
#     print(f"{student.na} from {student.ho}")

# def get_student():
    
#     na=input("Name: ")
#     ho=input("House: ")
#     return Student(na,ho)


# class Student:
#     def __init__(self, name, house):
#         self.na=name
#         self.ho=house
# def main():
#     student=get_student()
#     print(f"{student.na} from {student.ho}")

# def get_student():
    
#     na=input("Name: ")
#     ho=input("House: ")
#     return Student(na,ho)

# if __name__=="__main__":
#     main()



# class Student:
#     def __init__(self, name, house):
#         if not name:
#             raise ValueError("Missing Name")
#         if house not in ["GIIS","Rahul","Pawar","Podar"]:
#             raise ValueError("Invalid House")
#         self.na=name
#         self.ho=house
# def main():
#     student=get_student()
#     print(f"{student.na} from {student.ho}")

# def get_student():
    
#     na=input("Name: ")
#     ho=input("House: ")
#     return Student(na,ho)

# if __name__=="__main__":
#     main()






# class Student:
#     def __init__(self, name, house):
#         if not name:
#             raise ValueError("Missing Name")
#         if house not in ["GIIS","Rahul","Pawar","Podar"]:
#             raise ValueError("Invalid House")
#         self.na=name
#         self.ho=house
# def main():
#     student=get_student()
#     print(f"{student.firstn} {student.middlen} {student.lastn}from {student.ho}")

# def get_student():
    
#     firstn=input("Name: ")
#     middlen=input("MiddleName: ")
#     lastn=input("Last Name: ")    
#     ho=input("House: ")
#     return Student(firstn,middlen,lastn,ho)

# if __name__=="__main__":
#     main()


# ##################### String Method

# class Student:
#     def __init__(self, name, house):
#         if not name:
#             raise ValueError("Missing Name")
#         if house not in ["GIIS","Rahul","Pawar","Podar"]:
#             raise ValueError("Invalid House")
#         self.na=name
#         self.ho=house
#     def __str__(self):
#         return "a student           "
# def main():
#     student=get_student()
#     print(student)

# def get_student():
    
#     na=input("Name: ")
#     ho=input("House: ")
#     return Student(na,ho)

# if __name__=="__main__":
#     main()




# class Student:
#     def __init__(self, name, house):
#         if not name:
#             raise ValueError("Missing Name")
#         if house not in ["GIIS","Rahul","Pawar","Podar"]:
#             raise ValueError("Invalid House")
#         self.na=name
#         self.ho=house
#     def __str__(self):
#         return f"{self.na} from school {self.ho}"
# def main():
#     student=get_student()
#     print(student)

# def get_student():
    
#     na=input("Name: ")
#     ho=input("House: ")
#     return Student(na,ho)

# if __name__=="__main__":
#     main()


#################  Custom Methods

# class Student:
#     def __init__(self, name, house,patronus):
#         if not name:
#             raise ValueError("Missing Name")
#         if house not in ["GIIS","Rahul","Pawar","Podar"]:
#             raise ValueError("Invalid House")
#         self.na=name
#         self.ho=house
#         self.pa=patronus
#     def __str__(self):
#         return f"{self.na} from school {self.ho}"
    
#     def charm(self):
#         match self.pa:
#             case "Stag":
#                 return "🍕"
#             case "Otter":
#                 return "🍗"
#             case "prafee":
#                 return "🥩"
#             case _:
#                 return "/"

        
# def main():
#     student=get_student()
#     print("expect petronus")
#     print(student.charm())

# def get_student():
    
#     na=input("Name: ")
#     ho=input("House: ")
#     pa=input("Patronus")
#     return Student(na,ho,pa)

# if __name__=="__main__":
#     main()



# class Student:
#     def __init__(self, name, house):
#         if not name:
#             raise ValueError("Missing Name")
#         if house not in ["GIIS","Rahul","Pawar","Podar"]:
#             raise ValueError("Invalid House")
#         self.na=name
#         self.ho=house
#     def __str__(self):
#         return f"{self.na} from school {self.ho}"
# def main():
#     student=get_student()
#     student.ho="GIIs"   ################# Overwritten
#     print(student)

# def get_student():
    
#     na=input("Name: ")
#     ho=input("House: ")
#     return Student(na,ho)

# if __name__=="__main__":
#     main()


# class Student:
#     def __init__(self, name, house):
#         if not name:
#             raise ValueError("Missing Name")
#         self.na=name
#         self.ho=house
#     def __str__(self):
#         return f"{self.na} from school {self.ho}"
#     ##### getter
#     @property
#     def ho(self):
#         return self._ho
#     ### setter
#     @ho.setter
#     def ho(self,ho):
#         if ho not in ["GIIS","Rahul","Pawar","Podar"]:
#             raise ValueError("Invalid House")
#         self._ho=ho

# def main():
#     student=get_student()
#     # student.ho="GIIs"
#     print(student)

# def get_student():    
#     na=input("Name: ")
#     ho=input("House: ")
#     return Student(na,ho)

# if __name__=="__main__":
#     main()





class Student:
    def __init__(self, name, house):
        self.na=name
        self.ho=house

    def school(self,a,b):
        print("addition of a+b",a+b)
        print(self.na,self.ho)
        return(a+b)
studen=Student("raaya","giis")
a1=studen.school(5,6)
print(a1)
