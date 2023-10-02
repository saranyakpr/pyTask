
# 1. area of circle
area=int(input('Enter r value'))
circle=3.14*area*area
print('area of circle value is :',circle)

# 2. reverse order
firstName=input('Enter first name')
lastName=input('Enter last name')
print(firstName[::-1],end=' ')
print(lastName[::-1],end='  ')

# 3. reverse an integer
num=(input('Enter number'))
print(num[::-1], end=' ')

# 4.swap two number
a=1
b=2
temp=a
a=b
b=temp
print(a,b)

# 5.square value
square=int(input('Enter a number'))
print(square*square)

# 6.cube value
cube=int(input('Enter a number'))
print(cube*cube*cube)

# 7.square root value
root=int(input('Enter a number'))
print(root**.5)

# 8.lowercase to uppercase
name='saran'
print(name.upper())

# 9.join method
str3='white'
str4='wash'
str5=(str3,str4)
print('-'.join(str5))

# 10.without join method
str1='white'
str2='moon'
print(str1 + str2)

# 11.ascending
ascendingValue=['apple', 'mango', 'banana', 'orange']
ascendingValue.sort()
print(ascendingValue)

# 12.descending
descendingValue=['apple', 'mango', 'banana', 'orange']
descendingValue.sort(reverse=True)
print(descendingValue)







