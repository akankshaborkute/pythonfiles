menus=[['Egg Sandwich','Babel','Coffee'],
       ['BLT','PB&J','Turkey Sandwich'],
       ['Soup','Salad','Pizza','Tacco']]
print(menus[1][1])
print("##################################################")
menus={'BreakFast':['Egg Sandwich','Babel','Coffee'],
       'Lunch':['BLT','PB&J','Turkey Sandwich'],
       'Dinner':['Soup','Salad','Pizza','Tacco']}
print('BreakFast Menu:\t',menus['BreakFast'])
print('Lunch Menu:\t',menus['Lunch'])
print('Dinner Menu:\t',menus['Dinner'])
print("##################################################")
for i in menus:
    print(i,":",menus[i])

print("##################################################")
for name, menu in menus.items():
    print(name,":",menu)
print("##################################################")

contacts={
    'number':4,
    'Student':[
        {'name':'prafull','email':'prafull@gmail.com'},
        {'name':'raaya','email':'raaya@gmail.com'},
        {'name':'akanksha','email':'akanksha@gmail.com'},
        {'name':'aarush','email':'aarush@gmail.com'}
    ]
}

print('Student Emails:')
for student in contacts['Student']:
    print(student['email'])