dataList=[]
for i in range(3):
    name=input('enter username:')
    mobileNo=input('enter mobilno:')
    email=input('enter email:')
    mark1=(input('enter mark:'))
    mark2=(input('enter mark:'))
    mark3=(input('enter mark:'))
    mark4=(input('enter mark:'))
    mark5=(input('enter mark:'))
    marks=[mark1, mark2, mark3, mark4, mark5]
    dataDict={}
    dataDict.update({'name':name})
    dataDict.update({'mobileNo':mobileNo})
    dataDict.update({'email':email})
    dataDict.update({'marks':marks})
    dataList.append(dataDict)
print(dataList)

email=input('enter email')

for i in dataList:
    if email==i['email']:
        print(i['marks'])
       