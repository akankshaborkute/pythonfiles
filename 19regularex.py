import re
email=input("what's your email?").strip()
# if "@" and  "." in email:
#     print("valid")
# else:
#     print("invalid")

# username,domain=email.split("@")
# print(username+"\n",domain)
# if username and domain.endswith(".edu"):
#         print("valid")
# else:
#     print("invalid")
    
# if re.search(".*@.*",email):
#     print("valid")
# else:
#     print("invalid")    


# if re.search(".+@.+",email):
#     print("valid")
# else:
#     print("invalid")  

# if re.search(".+@.+.edu",email):
#     print("valid")
# else:
#     print("invalid")  

# if re.search(".+@.+\.edu",email):
#     print("valid")
# else:
#     print("invalid")  

# if re.search(r".+@.+\.edu",email):
#     print("valid")
# else:
#     print("invalid")      

# if re.search(r"^[^@]+@[^@]+\.edu$",email):
#     print("valid")
# else:
#     print("invalid")

# if re.search(r"^[a-zA-Z0-9_-]+@[a-zA-Z0-9_-]+\.edu$",email):
#     print("valid")
# else:
#     print("invalid")

# if re.search(r"^\w+@\w+\.edu$",email):
#     print("valid")
# else:
#     print("invalid")

# if re.search(r"^(\w|\s|\d)+@\w+\.edu$",email):
#     print("valid")
# else:
#     print("invalid")    