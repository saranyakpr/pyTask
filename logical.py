# 1.
num=int(input('enter the number:'))
emtDict={}
for i in range(num):
    emtDict.update({i:i*i})
print(emtDict)

# 2.
mark1=int(input('enter mark1'))
mark2=int(input('enter mark2'))
mark3=int(input('enter mark3'))
mark4=int(input('enter mark4'))
mark5=int(input('enter mark5'))
marks=mark1+mark2+mark3+mark4+mark5
print(marks)
avg=marks/5
print(avg)

# 3.
username=input('enter username')
email=input('enter email')

def myFun(username, email):
    return{'username:':username, 'email:':email}
print(myFun(username, email))

number=input('enter mobile number')
def myFun(number):
    return{'number:':number,}
print(myFun(number))

changenum=input('enter new number')
def changeFun(changenum):
    return{'username:':username, 'email:':email, 'newNumber:':changenum,}
print(changeFun(changenum))

# 4.
month=['january', 'february', 'march', 'april', 'may', 'june', 'july', 'august', 'september', 'october', 'november', 'december']
day=['sunday', 'monday', 'tuesday', 'wednusday', 'thursday', 'friday', 'saturday']
for i in month:
    for j in day:
        print(i, j)

# 5. 
newList=[]
for i in range(100,401):
    if i%2==0:
        newList.append(i)
print(newList)

# 6. 
givenList=[0, 10, [20, 30], 40, 50, [60, 70, 80], [90, 100, 110, 120]]
emtList=[]
for i in givenList:
    if type(i)==list:
        emtList.extend(i)
    else:
        emtList.append(i)
print(emtList)

# 7. 
list1=[{'math':90, 'science':92}, {'math':89, 'science':94}, {'math':92, 'science':88}]
math=[]
science=[]
for i in list1:
    math.append(i['math'])
    science.append(i['science'])
print(math)
print(science)

# 8.
studentDict={'Name':'Mahalakshmi', 'Age':24, 'Roll_No':101, 'Marks':[90,75, 80, 98, 75]}
newList=[]
for i in studentDict.items():
    newList.append(list(i))
print(newList)

# 9.
num1=input('enter num1')
num2=input('enter num2')
print(int(num2)+int(num1[::-1]))

# 10.
newList=[]
for i in range(1,3):
    newList.append(i**2)
print(newList)