# 1.create dictionaries
students={
    'student1':{
        'name':'saran',
        'age':21,
        'rollNo':121,
        'DOB':10/10/2001
    },
    'student2':{
        'name':'deepa',
        'age':21,
        'rollNo':121,
        'DOB':11/10/2001
    },
    'student3':{
        'name':'priya',
        'age':21,
        'rollNo':121,
        'DOB':12/10/2001
    },
    'student4':{
        'name':'amutha',
        'age':21,
        'rollNo':121,
        'DOB':12/10/2001
    },
    'student5':{
        'name':'moni',
        'age':21,
        'rollNo':121,
        'DOB':13/10/2001
    },
    'student6':{
        'name':'durga',
        'age':21,
        'rollNo':121,
        'DOB':14/10/2001
    },
    'student7':{
        'name':'saro',
        'age':21,
        'rollNo':121,
        'DOB':15/10/2001
    },
    'student8':{
        'name':'olivu',
        'age':21,
        'rollNo':121,
        'DOB':16/10/2001
    },
    'student9':{
        'name':'kalies',
        'age':21,
        'rollNo':121,
        'DOB':17/10/2001
    },
    'student10':{
        'name':'kani',
        'age':21,
        'rollNo':121,
        'DOB':18/10/2001
    }
}
print(students)

# 2.get the values from users
userDict={
    'name':input('enter name'),
    'mobile No':int(input('enter mobile number')),
    'email':input('enter email')
}
print(userDict)

# 3.two list into a dictionaries
list1=['mango', 'orange', 'apple']
list2=[150, 200, 250]
list3=dict.fromkeys(zip(list1, list2))
print(list3)

# 4.create dictionaries
mark={
    'name':'saran',
    'mark':[90, 91, 92, 93, 94]
}
print(mark)

# 5.append dictionaries
emptyList=[]
userDict={
    'name':input('enter your name'),
    'age':int(input('enter your age'))
}
addList=emptyList.append(userDict)
print(emptyList)

# 6.get user and fill dictionaires
empDict={
    'Employee id':123,
    'Name':'joe',
    'Mobile No':9876543210,
    'Year of Joining':2021
}
print(empDict)
print(empDict['Year of Joining'])
empDict.update({"Mobil No":8765432980})
print(empDict)



