# 1.
D1={'list1':[5, 9, 10, 20], 'list2':[16, 7, 4, 11], 'list3':[13, 10, 4, 8], 'list4':[7, 20, 6, 13]}
newList=[]
for i in D1.values():
   newList.extend(i)
   newList.sort()
print(newList)

# 2.
newList={}
for i in range(3):
    newDict={}
    name=input('enter name')
    score=int(input('enter score'))
    newDict.update({'name':name})
    newDict.update({'score':score})
    newList.update(newDict)
    for i,j in newList.items():
        if j>75:
            print(i)

# 3.
tem=[]
for i in range(1, 101):
    if i%2==0:
        if i%3==0:
            tem.append(i)
print(tem)

# 4.
for i in range(1, 101):
    if i%3==0:
        print(i,'this is Fizz')
    if i%5==0:
        print(i, 'this is Buzz')
    if i%3==0:
        if i%5==0:
            print(i, 'this is FizzBuzz')

# 5.
num=int(input('enter a number'))
if num%2==0:
    if num%8==0:
        if num%14==0:
            print('True')

