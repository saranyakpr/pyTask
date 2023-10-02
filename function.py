# get username and email
# username=input('enter username')
# email=input('enter email')

# def myFun(username, email):
#     return{'username:':username, 'email:':email}
# print(myFun(username, email))

# number=input('enter mobile number')
# def myFun(number):
#     return{'number:':number,}
# print(myFun(number))

# changenum=input('enter new number')
# def changeFun(changenum):
#     return{'username:':username, 'email:':email, 'newNumber:':changenum,}
# print(changeFun(changenum))
Student_list = [{"Name":"Mahalakshmi","Age":24 ,"Roll_NO": 101, "Marks":[90,75,80,98,75]},
                {"Name":"Nijanthan","Age":23 ,"Roll_NO": 102, "Marks":[90,75,80,98,65]},
                {"Name":"Selva","Age":22 ,"Roll_NO": 103, "Marks":[90,75,80,78,99]},
                {"Name":"Preethi","Age":22 ,"Roll_NO": 104, "Marks":[94,75,80,88,35]},
                {"Name":"Ajay","Age":23 ,"Roll_NO": 105, "Marks":[70,85,80,98,35]},          
                {"Name":"Anand","Age":26 ,"Roll_NO": 106, "Marks":[90,75,85,98,35]},
                {"Name":"Pavitran","Age":21 ,"Roll_NO": 107, "Marks":[80,98,35,90,75]},
                {"Name":"Kumar","Age":25 ,"Roll_NO": 108, "Marks":[90,80,98,35,75]},
                {"Name":"Saranya","Age":26 ,"Roll_NO": 109, "Marks":[75,80,90,98,35]},
                {"Name":"Jeffin","Age":22 ,"Roll_NO": 110, "Marks":[98,35,90,75,80]}]
def fun1():
    name=input('enter your name')
    age=int(input('enter your age'))
    rollno=int(input('enter your rollno'))
    mark1=int(input('enter your tamil mark'))
    mark2=int(input('enter your english mark'))
    mark3=int(input('enter your maths mark'))
    mark4=int(input('enter your science mark'))
    mark5=int(input('enter your social mark'))
    mark=[mark1, mark2, mark3, mark4, mark5]
    studentDetail={'name':name, 'age':age, 'rollno':rollno, 'mark':mark}
    return studentDetail

def fun2():
    studentData=fun1()
    Student_list.append(studentData)
    return Student_list
print(fun2())