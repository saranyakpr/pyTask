emtList=[{"Name":"Mahalakshmi","Age":24 ,"Roll_NO": 101, "Marks":[90,75,80,98,75]}, 
         {"Name":"Nijanthan","Age":23 ,"Roll_NO": 102, "Marks":[90,75,80,98,65]}, 
         {"Name":"Selva","Age":22 ,"Roll_NO": 103, "Marks":[90,75,80,78,99]}, 
         {"Name":"Preethi","Age":22 ,"Roll_NO": 104, "Marks":[94,75,80,88,35]},
         {"Name":"Ajay","Age":23 ,"Roll_NO": 105, "Marks":[70,85,80,98,35]}, 
         {"Name":"Anand","Age":26 ,"Roll_NO": 106, "Marks":[90,75,85,98,35]}, 
         {"Name":"Pavitran","Age":21 ,"Roll_NO": 107, "Marks":[80,98,35,90,75]}, 
         {"Name":"Kumar","Age":25 ,"Roll_NO": 108, "Marks":[90,80,98,35,75]}, 
         {"Name":"Saranya","Age":26 ,"Roll_NO": 109, "Marks":[75,80,90,98,35]}, 
         {"Name":"Jeffin","Age":22 ,"Roll_NO": 110, "Marks":[98,35,90,75,80]}]
studentData=[]
sum=0
for i in emtList:
    studentDict={}
    name=i.get('Name')
    age=i.get('Age')
    Roll_No=i.get('Roll_NO')
    Marks=i.get('Marks')
    for j in i['Marks']:
        sum+=j
        avg=sum/5
        studentDict.update({'Name':name})
        studentDict.update({'Age':age})
        studentDict.update({'Roll_No':Roll_No})
        studentDict.update({'Average':avg})
        studentData.append(studentDict)
print(studentData)









