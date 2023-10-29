#List:
#Allows duplicate 
#any type of data can be stored
#we can modify the list item, we can add or remove insert(), append(), extend(),pop()
subjectsList=["english", "tamil", "maths", "science"]
print(type(subjectsList))
print(subjectsList)
#add the last elements of a list
subjectsList.append("social")
#any type of data can be stored in List
subjectsList.append(6)
subjectsList.append(True)
print(subjectsList)
#insert the elements in index
subjectsList.insert(0,'computerscience')
print(subjectsList)
#Replace the elements in index
subjectsList[3]="physics"
print(subjectsList)
#Remove the elements in index
subjectsList.pop(5)
print(subjectsList)
#merge the elements in list
subjectsList1=["chemistry","geography","biology"]
subjectsList.extend(subjectsList1)
print(subjectsList)