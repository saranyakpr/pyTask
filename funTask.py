# 1. find the maximun of three numers
# a=input('enter 1st number')
# b=input('enter 2nd number')
# c=input('enter 3rd number')
# def maxNum():
#     if(a>b):
#        if(a>c):
#           print('a is maximum number', a)
#        else:
#           print('c is maximum number', c)
#     elif(b>c):
#        print('b is maximum number', b)
#     else:
#        print('c is maximum number', c)
# maxNum()

# 2.sum all the numbers in a list
# sumList=[1, 2, 3, 4, 5]
# def sumFun(sumList):
#     sum=0
#     for i in sumList:
#         sum+=i
#     return sum
# print(sumFun(sumList))

# 3. counts the number of upper and lower
# def caseFun(stringName):
#     stringName='Saran'
#     upperCase=0
#     lowerCase=0
#     for i in stringName:
#         if i.isupper():
#             upperCase+=1
#         else:
#             lowerCase+=1
#     print('Uppercase count is:', upperCase, 'Lowercase count is:', lowerCase)
# caseFun('Saran')

# 4. return new list with distinct element
# def distFun(l):
#     newDistList=[]
#     for a in l:
#         if a not in newDistList:
#             newDistList.append(a)
#     return newDistList
# print(distFun([1, 2, 3, 4, 5, 1, 2]))

# 5.squares of the numbers between 1-30
# def squareFun():
#     squareList=[]
#     for b in range(1, 30):
#         squareList.append(b**2)
#     print(squareList)
# squareFun()

# 6.dictionaries
# def dictFun():
#     dictList={
#         'username':'saran',
#         'age':22,
#         'DOB':2001,
#     }
#     print(dictList.get('DOB'))
#     dictList.update({'year':2002})
#     print(dictList)
#     dictList['year']='2020'
#     print(dictList)
# dictFun()

# 7.create a list and add 2name using append and arrange ascending and descending order
# def listFun():
#     newList=['saran', 'raja', 'selvi']
#     newList.append('sakthi')
#     newList.append('satheesh')
#     newList.sort()
#     print(newList)
# listFun() 

# 8.get month and date another list 
# def monthFun():
#     month=['January', 'February', 'March', 'April', 'May', 'June', 'July', 'August', 'September', 'October', 'November', 'December']
#     day=['sunday', 'monday', 'tuesday', 'wednesday', 'thursday', 'friday', 'saturday']
#     for m in month:
#         if m in month:
#             for n in day:
#                 o=m,n
#                 o=list(o)
#                 print(o)
# monthFun()

# 9.get 5 values from user the dictionaries and convert list
# def listFun():
#     username=input('enter username')
#     age=int(input('enter age'))
#     grade=int(input('enter grade'))
#     gender=input('enter gender')
#     mobileNo=int(input('enter mobile number'))
#     newDict={'username':username, 'age':age, 'grade':grade, 'gender':gender, 'mobile':mobileNo}
#     print(newDict)
#     createList=[]
#     for d in newDict.values():
#         createList.append(d)
#     print(createList)
# listFun()

# 10.get username, email, mobileNo convert dict
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


# def funA():
#     username=input('enter username')
#     email=input('enter email')
#     num=input('enter mobile number')
#     DictList={'username':username, 'email':email, 'mobileNo':num}
#     return DictList
# def funB():
#     newList=[]
#     newDict=funA()
#     newList.append(newDict)
#     return newList
# value=funB()
# print(value)

# def createDetail():
#      createDatas=[]
#      for i in range(3):
#         name=input('enter your name')
#         age=int(input('enter your age'))
#         rollno=int(input('enter your rollno'))
#         mark1=int(input('enter your tamil mark'))
#         mark2=int(input('enter your english mark'))
#         mark3=int(input('enter your maths mark'))
#         mark4=int(input('enter your science mark'))
#         mark5=int(input('enter your social mark'))
#         mark=['mark1', 'mark2', 'mark3', 'mark4', 'mark5']
#         studentDetail={'name':name, 'age':age, 'rollno':rollno, 'mark':mark}
#         createDatas.append(studentDetail)
#      return createDatas

# def createList(studentList):
#     datas=createDetail()
#     studentlist.append(datas)
#     return studentlist
# print(createList(studentlist))
    

    






