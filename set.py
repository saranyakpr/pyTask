# 1.create set 
newSet={'html', 'css', 'js'}
print(newSet)

# 2.iterate over sets
for i in newSet:
    print(i)

# 3.remove items from set
delSet={'html', 'css', 'js'}
deleSet=delSet.remove('css')
print(type(delSet))

# 4.add items in set
setAdd={'saran', 'selvi'}
setAdd.add('ramaraja')
print(setAdd)

# 5.create union of sets
setUnion1={1, 2, 3}
setUnion2={4, 5, 6}
setUnion3=setUnion1.union(setUnion2)
print(setUnion3)

# 6.remove all elements from set
setRemove={'saran', 'selvi', 'ramaraja', 'sakthi', 'satheesh'}
setRemove.clear()
print(setRemove)

# 7.find the length of set
setRemove1={'saran', 'selvi', 'ramaraja', 'sakthi', 'satheesh'}
print(len(setRemove1))

# 9.convert a tuple to a list
creatTup=('red', 'orange', 'blue')
creatTup1=str(creatTup)
print(creatTup1)

# 10.vaue of rectangle, cylinder
# rectangle= A=wl
l=3
w=5
area=w*l
print(area)

# cylinder vol=22/7*r*h*2
r=5
h=6
vol=22/7*r*h*2
print(vol)

