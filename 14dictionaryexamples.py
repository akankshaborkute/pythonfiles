dicti={"name":"prafull","sname":"borkute","school":"shivaji"}
print(dicti["school"])
dicti["school"]="chandur"
print(dicti["school"])
print(dicti)
dicti1={}
dicti1["subject"]="Marathi"
dicti1["school"]="Shivaji"
dicti1["place"]="Morshi"

print(dicti1["place"])

print(dicti1.get("school"))
fh=dicti1.get("place")
print(fh)
if (dicti1.get("school")):
    print("found")


current_mov={'The Girich':'11:00am','gadar0':"12:00pm","mi7":'13:00am','omg':'3:00pm'}
print("We are showing following movies")
for i in current_mov:
    print(i,current_mov[i])
movie=input("Waht movie u would like to watch")
showtime=current_mov.get(movie)
if showtime==None:
    print("requested movie is'n playin")
else:
    print(movie,"is playing at",showtime)    
